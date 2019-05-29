import os

from . import env
PLATFORM = env.get('PLATFORM', 'IOS')
# shortcuts
IS_ANDROID = PLATFORM == 'ANDROID'
IS_IOS = PLATFORM == 'IOS'
