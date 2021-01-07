import json
import unittest

import ThreefoldLoginPkg
import ThreefoldLoginPkg.threefold_login
from ThreefoldLoginPkg.utils.crypto import generate_key_pair, get_ed_pk_in_curve
from ThreefoldLoginPkg.utils.parse import parse_signed_attempt_from_url

protocol = 'https:'
rawHost = 'login.staging.jimber.org'

three_fold_api_host = protocol + '//' + rawHost
app_id = 'test.threefoldlogin'
seed_phrase = 'calm science teach foil burst until ' \
              'next mango hole sponsor fold bottom ' \
              'cousin push focus track truly tornado ' \
              'turtle over tornado teach large fiscal'
redirect_url = 'https://test-bot-front-end.io'
kyc_backend_url = 'https://openkyc.staging.jimber.org'

state = 'glsqIjWpvX24tpT6A3xbmvbr5FBJh1Pk'

test_url = 'https://login.staging.jimber.org/?state=glsqIjWpvX24tpT6A3xbmvbr5FBJh1Pk&appid=test.threefoldlogin&publickey=haPnjRJSFG1mk388ZCk9ybi0h%2FYx0QkOzPQLFVoYOBw%3D&redirecturl=https%3A%2F%2Ftest-bot-front-end.io'
test_url_with_scope = 'https://login.staging.jimber.org/?state=glsqIjWpvX24tpT6A3xbmvbr5FBJh1Pk&appid=test.threefoldlogin&publickey=haPnjRJSFG1mk388ZCk9ybi0h%2FYx0QkOzPQLFVoYOBw%3D&redirecturl=https%3A%2F%2Ftest-bot-front-end.io&scope=%7B%22doubleName%22%3Atrue%2C%22email%22%3Afalse%7D'
test_redirect_url = 'https://test.threefoldlogin/https://test-bot-front-end.io?signedAttempt=%7B%22signedAttempt%22%3A%22OQbbjNSmkvxtVDcjcnbN%2BAQjkiZaruNCQ2arNQ01I1atiK4rcFpBzxm3693WtThY3yA6ChsgbQUA7WpLRvaUBnsic2lnbmVkU3RhdGUiOiJnbHNxSWpXcHZYMjR0cFQ2QTN4Ym12YnI1RkJKaDFQayIsImRhdGEiOnsibm9uY2UiOiJndEdUa2dLdjBHa21mN2E5RWd0MGI5bmxOS0kzR2pYTCIsImNpcGhlcnRleHQiOiJoU2pyNGRydUlJSE5yd3Y0ZkZNWmRTUWNrcG5mZ09GU2svNVBJZUxMOHA4Smdyc09MUm9BNVpCc2xMcnI3SjVsYm1QamlZVTZXN1cvIn0sInNlbGVjdGVkSW1hZ2VJZCI6MTA1LCJkb3VibGVOYW1lIjoiaWZyLjNib3QiLCJyYW5kb21Sb29tIjoiZGY5NzFjZjAtMDkzMi00NGJhLWI1YTktYzg3Y2RkOGUxNmJjIiwiYXBwSWQiOiJ0ZXN0LnRocmVlZm9sZGxvZ2luIn0%3D%22%2C%22doubleName%22%3A%22ifr.3bot%22%7D'
test_signed_attempt = 'OQbbjNSmkvxtVDcjcnbN+AQjkiZaruNCQ2arNQ01I1atiK4rcFpBzxm3693WtThY3yA6ChsgbQUA7WpLRvaUBnsic2lnbmVkU3RhdGUiOiJnbHNxSWpXcHZYMjR0cFQ2QTN4Ym12YnI1RkJKaDFQayIsImRhdGEiOnsibm9uY2UiOiJndEdUa2dLdjBHa21mN2E5RWd0MGI5bmxOS0kzR2pYTCIsImNpcGhlcnRleHQiOiJoU2pyNGRydUlJSE5yd3Y0ZkZNWmRTUWNrcG5mZ09GU2svNVBJZUxMOHA4Smdyc09MUm9BNVpCc2xMcnI3SjVsYm1QamlZVTZXN1cvIn0sInNlbGVjdGVkSW1hZ2VJZCI6MTA1LCJkb3VibGVOYW1lIjoiaWZyLjNib3QiLCJyYW5kb21Sb29tIjoiZGY5NzFjZjAtMDkzMi00NGJhLWI1YTktYzg3Y2RkOGUxNmJjIiwiYXBwSWQiOiJ0ZXN0LnRocmVlZm9sZGxvZ2luIn0='
test_signed_email_identifier = 'LouB5RT/tmQxfW1M2unm/khafCu0ib4cpsKpm9ETwKgjlhhb4cV/Qw5T0vMMnEpcOKS0Bq0pBjFMOkEgGBnYDXsgImVtYWlsIjogIm1hdGhpYXMuZGUud2VlcmR0QGdtYWlsLmNvbSIsICJpZGVudGlmaWVyIjogInRhaWsuM2JvdCIgfQ==';


class TestThreefoldLoginPkg(unittest.TestCase):

    def setUp(self) -> None:
        self.login = ThreefoldLoginPkg.threefold_login.ThreefoldLogin(
            three_fold_api_host,
            app_id,
            seed_phrase,
            redirect_url,
            kyc_backend_url)

    def test_constructor(self):
        test_three_fold_api_host = ''
        test_app_id = ''
        test_seed_phrase = ''
        test_redirect_url = ''
        test_kyc_backend_url = ''

        login = ThreefoldLoginPkg.threefold_login.ThreefoldLogin(
            test_three_fold_api_host,
            test_app_id,
            test_seed_phrase,
            test_redirect_url,
            test_kyc_backend_url)

        self.assertIsInstance(login, ThreefoldLoginPkg.threefold_login.ThreefoldLogin)

    def test_getters(self):
        test_three_fold_api_host = 'test0'
        test_app_id = 'test1'
        test_seed_phrase = 'test2'
        test_redirect_url = 'test3'
        test_kyc_backend_url = 'test4'

        login = ThreefoldLoginPkg.threefold_login.ThreefoldLogin(
            test_three_fold_api_host,
            test_app_id,
            test_seed_phrase,
            test_redirect_url,
            test_kyc_backend_url)

        self.assertEqual(login.three_fold_api_host, test_three_fold_api_host)
        self.assertEqual(login.app_id, test_app_id)
        self.assertEqual(login.seed_phrase, test_seed_phrase)
        self.assertEqual(login.redirect_url, test_redirect_url)
        self.assertEqual(login.kyc_backend_url, test_kyc_backend_url)

    def test_generate_login_url(self):
        login_url = self.login.generate_login_url(state)
        self.assertEqual(login_url, test_url)

    def test_generate_login_url_with_scope(self):
        scope = json.dumps({'doubleName': True, 'email': False}, separators=(',', ':'))
        login_url = self.login.generate_login_url(state, {'scope': scope})
        self.assertEqual(login_url, test_url_with_scope)

    def test_parse_and_validate_the_signed_attempt_redirect_url(self):
        data = self.login.parse_and_validate_redirect_url(test_redirect_url, state)
        self.assertEqual(data, {
            'profile': {
                'email': {
                    'email': 'hd@jd.so',
                    'sei': None
                }
            },
            'randomRoom': 'df971cf0-0932-44ba-b5a9-c87cdd8e16bc',
            'selectedImageId': 105
        })

    def test_verify_my_signed_email_idenfier(self):
        emailData = self.login.verify_signed_email_idenfier(test_signed_email_identifier)
        self.assertEqual(emailData, {
            "email": 'mathias.de.weerdt@gmail.com',
            "identifier": 'taik.3bot',
        })

    def test_is_mail_verified(self):
        isVerified = self.login.is_email_verified(test_signed_email_identifier)
        self.assertEqual(isVerified, True)


class TestCrypto(unittest.TestCase):

    def test_generate_key_pair(self):
        key_pair = generate_key_pair(seed_phrase)
        self.assertEqual(True, True)

    def test_should_be_able_to_get_a_edkey_key(self):
        key_pair = generate_key_pair(seed_phrase)
        public_key = get_ed_pk_in_curve(key_pair[0])
        self.assertEqual(public_key, b'haPnjRJSFG1mk388ZCk9ybi0h/Yx0QkOzPQLFVoYOBw=')


class TestParse(unittest.TestCase):

    def test_parse_signed_attempt_from_url(self):
        data = parse_signed_attempt_from_url(test_redirect_url, state)
        self.assertEqual(data['signedAttempt'], test_signed_attempt)
        self.assertEqual(data['doubleName'], 'ifr.3bot')


if __name__ == '__main__':
    unittest.main()
