import random
import os
import json

FAKE_SMS_CODE = 1313
FAKE_NUMBER = "+79000009998"
FAKE_ADMIN_NUMBER = "+79990000009"
REGION = "Russia"
FAKE_INVITE_CODE = "KEKE"
BIO_TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et " \
           "dolore magna aliqua. Ut enim ad minim veniam, quis nostru"
EMPTY_BIO_TEXT = "Add a bio to your profile!"
REPORT_REASON_TEXT = "This is not appropriate for the platform"

WAIT = dict(ELEMENT=10,
            TEXT=10,
            ALERT=20,
            PAGE=30)

SCREENSHOT_FOLDER_PATH = os.path.abspath('.')

GIF_IDS = ["3OBcAfnMsWKqgWWRlf", "uVPv3hrAa4ehQeRHvk", "3fiimcA0K0ifzoL7FF", "1iscJqlNpsW5zk8UFq", "MnFxIouXendMTUHjQg",
           "5tdoAbeKnIK2g0xQHo", "1BdJd24oEwvuSvXYb0", "8mt4uVOhczfwkc2KfD", "3HELB2Qwfu9dV1ZGYY", "9Pk3Y2QCF1fR7TyXqZ",
           "7IYE22rKh7dnt4QNBV", "dexMDPoiX5ugfw8tNP", "5pT47Vs6g1ZxGDK6im", "oFI7FttD0iC8V2Iqmy", "e9PGY2KhfzZ2ayw9nH",
           "9PrnwcV8IkvhCGl5Hn", "Zvx9ttT97cevkbyVik", "fBG7UnBi7QtePFHEnk", "31UDILmnnQOjnKKoKB", "SHP92Zpivx9Pfr1geG",
           "xlLy6mi4V03IAr2kWn", "ejRo0le6WWLvy9OSOe", "1dIoHBbyFpWzK0Div8", "1zhI2P2OaLavdbUsrI", "3DudglxvlDmJfCVQjL"]


class AcesUser(object):
    """
        This class contains parameters of simple User for testing
            :first_name - first name of User
            :last_name - last name of User (permanently "Contact")
            :username - his Username optional()
            :phone - digits of his phone number
            :birth_date
            :data - some information, used by test
    """
    def __init__(self, first_name='Ozeny', last_name='Kotikov Jr.', username=None,
                 phone=None, email="iphone@techops.ru", birth_date='01012001', user_id=None, data=None):
        self.first_name = first_name
        self.last_name = last_name

        if username is None:
            random_number = '{:03d}'.format(random.randrange(1, 9999999999))
            self.username = ("Oz" + "Kot" + random_number)
        else:
            self.username = username

        if phone is None:
            self.phone = self.generate_random_phone_number()
        else:
            self.phone = phone

        self.email = email

        self.birth_date = birth_date
        self.user_id = user_id
        self.data = data

    def generate_random_phone_number(self):
        """
        Generates random US or RU phone number

        :return: generated number
        """
        script_dir = os.path.dirname(__file__)
        fn = os.path.join(script_dir, 'usa_area_codes.json')

        with open(fn) as f:
            data = json.load(f)

        usa_area_codes = data['usa_area_codes']

        random_number = [
            "+1" + str(random.sample(usa_area_codes, 1)) + str(random.randrange(2000000, 9999999)),
            "+7" + str(random.randrange(9000000000, 9999999999))
        ]

        return random.sample(random_number, 1)


FAQ_TEXT_TO_COMPARE = "“How do I create an ace?”"

PRIVACY_POLICY_TEXT_TO_COMPARE = "Personal Information includes the following information:"

TOS_TEXT_TO_COMPARE = "You may use the Services only if you agree to form a binding contract with Aces and are not a " \
                      "person barred from receiving services under the laws of the applicable jurisdiction. " \
                      "In any case, you must be at least 13 years old to use the Services. If you are between " \
                      "13 and 18 years old, you must have your parent or legal guardian’s permission to use the " \
                      "Services. If you are accepting these Terms and using the Services on behalf of a company, " \
                      "organization, government, or other legal entity, you represent and warrant that you are " \
                      "authorized to do so."