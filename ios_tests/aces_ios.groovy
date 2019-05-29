node('mini-ssh') {
    def appium_pid = null
    sh "mkdir aces-ios || True"
    stage('Pulling aces') {
        checkout( [
          $class: 'GitSCM',
          branches: [[name: "${APP_RC_TAG}"]],
          browser: [
            $class: 'GithubWeb',
            repoUrl: 'https://github.com/aces/aces-ios'],
          doGenerateSubmoduleConfigurations: false,
          extensions: [
            [$class: 'CleanBeforeCheckout'],
            [$class: 'PruneStaleBranch'],
            [$class: 'RelativeTargetDirectory',
              relativeTargetDir: "${WORKSPACE}/aces-ios"]],
          submoduleCfg: [],
          userRemoteConfigs: [
            [credentialsId: '078fcf40-b662-41ea-af07-7185a9ca',
            url: 'git@github.com:aces/aces-ios.git']]]
        )
        sh """
            cd aces-ios
            pod install --repo-update

            """
    }

    stage('Prepare testing'){
      checkout( [
        $class: 'GitSCM',
        branches: [[name: "${TEST_BRANCH}"]],
        browser: [
          $class: 'GithubWeb',
          repoUrl: 'https://github.com/aces/aces-tests'],
        doGenerateSubmoduleConfigurations: false,
        extensions: [
          [$class: 'RelativeTargetDirectory',
            relativeTargetDir: "${WORKSPACE}/aces-tests"],
          [$class: 'CleanBeforeCheckout'],
          [$class: 'PruneStaleBranch']],
        submoduleCfg: [],
        userRemoteConfigs: [
          [credentialsId: '078fcf40-b662-41ea-af07-7185a9ca',
          url: 'git@github.com:aces/aces-tests.git']]]
      )
      sh """
          brew install libjpeg
          |python3 -m venv ${WORKSPACE}/venv --clear
          |source ${WORKSPACE}/venv/bin/activate
          |pip3 install -r ${WORKSPACE}/aces-tests/requirements.txt
          """.stripMargin("|")
      sh "mkdir report || True"
      appium_pid = sh(
          script:"/usr/local/bin/appium --port=4736 > appium_server.log & \n echo \$!",
          returnStdout: true
      ).trim()
      println "Appium pid is: ${appium_pid}"
    }

    stage('Testing') {
      ansiColor('xterm') {
        try {
          sh """
              source ${WORKSPACE}/venv/bin/activate
              py.test -s --html=report/index.html -v aces-tests/ios_tests/tests/ --rerun 1 --workspace=aces-ios --device="${DEVICE_NAME}" --sdk=iphonesimulator${SDK} --ios-version=${IOS_VERSION} -k="${PYTEST_EXCL}  --appium-port=4736"
              """
          currentBuild.result = "SUCCESS"
          emailext(
            body: "Status of build: PASSED, JOB_NAME: ${env.JOB_NAME}, BUILD_NUMBER: ${env.BUILD_NUMBER}, BUILD_URL: ${env.BUILD_URL}",
            subject: "PASSED: ${env.JOB_NAME} ${env.BUILD_NUMBER}",
            to: 'andrey.egorov@techops.ru'
          )
        } catch (Exception err) {
          currentBuild.result = "FAILURE"
          emailext(
            body: "Status of build: FAILED, JOB_NAME: ${env.JOB_NAME}, BUILD_NUMBER: ${env.BUILD_NUMBER}, BUILD_URL: ${env.BUILD_URL}",
            subject: "FAILED: ${env.JOB_NAME} ${env.BUILD_NUMBER}",
            to: 'aino@techops.ru, andrey.egorov@techops.ru'
          )
        }
        sh """
          rm -rf ${WORKSPACE}/report/assets/style.css
          cp ${WORKSPACE}/aces-tests/ios_tests/ios_style.css ${WORKSPACE}/report/assets/style.css
        """
        println "Kill our appium server"
        sh "kill -9 ${appium_pid} || True"
        // Make fancy html report from pytest output
        publishHTML([
          allowMissing: false,
          alwaysLinkToLastBuild: false,
          keepAll: true,
          reportDir: 'ios_tests/report/',
          reportFiles: 'index.html',
          reportName: 'Aces test report',
          reportTitles: ''])

      }
    }
}
