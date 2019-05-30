# About

This is just sample code and README from project I worked on. 


## Installation

Xcode should be installed on your system.

1. Install and setup aces-ios project to the next directory

````
https://github.com/aces/aces-ios
````

2. Setup Appium on your Mac

Tutorial:
````
https://gist.github.com/maggiesavovska/d2d47345c92fdf70ed4ec10ebb34c170
https://techsouljours.blogspot.com/2018/08/install-appium-on-mac.html (full setup for real device)
````

3. Python 3 is required to run tests.
It is also recomended to use virtualenv to isolate test environment.
```
brew install python3
pip install virtualenv
```

4. Create virtualenv and install requirements for tests.
```bash
virtualenv --python=python3 .venv
# Activates virtualenv. Activating it is not a requirement.
# Command below can be run without it just like this:
# .venv/bin/pip install -r requirements.txt
source .venv/bin/activate
pip install -r requirements.txt
```

## How to run iOS tests
---

To start appium server use new console or standalone application.
```
appium
```

Choose platform ```export PLATFORM=IOS``` or ```ANDROID``` (you can add environmental variables in PYCHARM in test configuration)

When appium started, run tests in your virtual environment (simulator):
```bash
py.test -s ios_tests/tests/ -v --workspace=../aces-ios --sdk={current SDK version} --ios-version={needed iOS version}
```
