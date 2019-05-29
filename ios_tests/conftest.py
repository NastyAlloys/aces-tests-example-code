import pytest
import os
import pprint
import shutil
import subprocess
from datetime import datetime
import plistlib
import time

from caesar.common.settings import IOS_APP, DR_MOBILE
from caesar.core.driver import Driver
from caesar.mobile.mobile_driver import MobileDriver
from caesar.tools.utils import ScreenShot
from common.settings import SCREENSHOT_FOLDER_PATH as screen_path

WDA_ORG_ID = '2279GKWVGH'
SIGN_ID = 'iPhone Developer'

timestamp = datetime.now().strftime('%H.%M.%S')
screenshot_path = os.path.join(screen_path, 'report')


def pytest_addoption(parser):
    parser.addoption("--workspace", help="Path to app's source code.")
    parser.addoption("--sdk", help="SDK to use for build.")
    parser.addoption("--appium-port", default="4736", help="Port of Appium server for execution")
    parser.addoption("--device", default='iPhone 7', help="Device/emulator to run tests")
    parser.addoption("--wda-port", default=8200, help="Port of Appium server for execution")
    parser.addoption("--ios-version", help="iOS version to test build")
    parser.addoption("--platform", default="IOS")


def git_commit(workdir):
    cmd = 'GIT_DIR={0}/.git GIT_WORK_TREE={0} git describe --always'.format(workdir)
    out = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE)
    return out.stdout.decode().strip()


def build_app(workdir, sdk, udid, ios_ver):
    derivedir = os.path.join(os.getcwd(), '.build', ios_ver, git_commit(workdir))
    app = os.path.join(derivedir, 'Build/Products/Debug-iphonesimulator/Aces.app')
    pprint.pprint("THIS IS PATH!" + app)
    # app already built
    if os.path.isdir(app):
        return app

    cmd = ' '.join([
        'xcodebuild',
        '-workspace {}/Aces.xcworkspace'.format(workdir),
        '-scheme aces',
        '-derivedDataPath {}'.format(derivedir),
        '-sdk {}'.format(sdk),
        '-destination "id={}"'.format(udid),
        'clean build',
        '| xcpretty' if bool(shutil.which("xcpretty")) else '',
    ])

    subprocess.run(cmd, shell=True, check=True)
    return app


def get_udid(ios_ver, device='iPhone 7'):
    cmd = 'instruments -s devices'
    udid = None
    output = str(subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE)).split("\\n")
    for line in output:
        if '{0} ({1})'.format(device, ios_ver) in line:
            udid = (line.split('[')[1].split(']')[0])
            break
    print('UDID of device {0} is {1}'.format(device, udid))
    return udid


def change_plist_file(wrkdir):
    """
    changing plist to not send sms during/login/registration

    :param wrkdir: project workspace
    """
    fn = '{}/Sources/InfoPlists/Info.plist'.format(wrkdir)

    with open(fn, 'rb') as f:
        plist_content = plistlib.load(f)
        if not plist_content['SkipSmsDuringLogin']:
            plist_content['SkipSmsDuringLogin'] = True
    with open(fn, 'wb') as f:
        plistlib.dump(plist_content, f)


def pytest_configure(config):
    wrkdir = config.getoption("--workspace")
    if not wrkdir:
        pytest.fail("Missing --workspace option.")

    change_plist_file(wrkdir)

    sdk = config.getoption("--sdk")
    if not sdk:
        pytest.fail(
            "Missing --sdk option. See full list of "
            "SDK's: xcodebuild -showsdks")

    ios_ver = config.getoption("--ios-version")
    if not ios_ver:
        pytest.fail(
            "Missing --ios_version option. See full list of "
            "supported devices: instruments -s devices")

    appium_port = config.getoption("--appium-port")
    device = config.getoption("--device")
    localport = config.getoption("--wda-port")

    udid = get_udid(ios_ver, device)

    app = build_app(wrkdir, sdk, udid, ios_ver)

    IOS_APP.update(
        app=app,
        udid=udid,
        platformVersion=ios_ver,
        deviceName=device,
        fullReset=False,
        wdaLocalPort=localport,
        # Values below are required to build WebDriverAgentRunner
        updatedWDABundleId='us.project101.WebDriverAgentRunner',
        xcodeOrgId=WDA_ORG_ID,
        xcodeSigningId=SIGN_ID,
    )

    com_executor = 'http://127.0.0.1:{}/wd/hub'.format(appium_port)

    DR_MOBILE.update(
        command_executor=com_executor,
        desired_capabilities=IOS_APP)

    pytest.platform = 'IOS'

    pprint.pprint(IOS_APP)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.failed:
        extra.append(
            pytest_html.extras.html(
                '<div class="image"><img src="screenshot/{0}_{1}.png"/>'
                '</div>'.format(item.name, timestamp)))
        report.extra = extra
    setattr(item, "rep_" + report.when, report)

# FIXTURES BLOCK


@pytest.fixture(scope='function', autouse=True)
def test_setup(request):
    Driver.driver = MobileDriver(**DR_MOBILE).driver
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    setup_failed = hasattr(request.node, 'rep_setup'
                           ) and request.node.rep_setup.failed
    call_failed = hasattr(request.node, 'rep_call'
                          ) and request.node.rep_call.failed
    if setup_failed or call_failed:
        time.sleep(1)
        screenshot_name = "{0}_{1}".format(request.node.name, timestamp)
        ScreenShot(screenshot_path).save_screenshot(screenshot_name)

    print('System was reset.')

