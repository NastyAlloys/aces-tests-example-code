from enum import Enum


class Endpoints(Enum):
    BASE_STRING = "https://api.com/api"
    PHONE_SEND_CONFIRMATION_CODE = BASE_STRING + "/v1/phone/send/"
    PHONE_VERIFY_CODE = BASE_STRING + "/v1/phone/verify/"

    CREATE_ACE = BASE_STRING + "/v4/aces/"
    GIPHY_UPLOAD = BASE_STRING + "/v1/media/giphy/"
    USER_PROFILE = BASE_STRING + "/v1/profile/self/"
    CREATE_FLIP = BASE_STRING + "/v5/aces/react/"
