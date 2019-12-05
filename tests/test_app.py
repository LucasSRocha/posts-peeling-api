import unittest

from flask import url_for

from app.app import app
from app.app import get_user_info


class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_get_root_no_email(self):
        response = self.client.get(url_for('index'))

        self.assertEqual(response.status_code, 200)

    def test_get_root_content_type(self):
        response = self.client.get(url_for('index'))

        self.assertIn('text/html', response.content_type)

    def test_get_root_form(self):
        response = self.client.get(url_for('index'))

        self.assertIn('<form name="email-submit-form"', response.data.decode())

    def test_post_root_no_email(self):
        response = self.client.post(url_for('index'))

        self.assertEqual(response.status_code, 400)
        self.assertIn('user not informed', response.data.decode().lower())

    def test_post_root_valid_email(self):
        data = {'email': 'Sherwood@rosamond.me'}

        response = self.client.post(url_for('index'), data=data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)

    def test_post_root_invalid_email(self):
        data = {'email': 'vo@testar.email'}

        response = self.client.post(url_for('index'), data=data)

        self.assertEqual(response.status_code, 404)
        self.assertIn('user not found', response.data.decode().lower())
        self.assertIn('application/json', response.content_type)

    def test_get_user_info_valid(self):
        email = 'Sherwood@rosamond.me'
        expected_response = {
                            "id": 8,
                            "name": "Nicholas Runolfsdottir V",
                            "username": "Maxime_Nienow",
                            "email": "Sherwood@rosamond.me",
                            "address": {
                              "street": "Ellsworth Summit",
                              "suite": "Suite 729",
                              "city": "Aliyaview",
                              "zipcode": "45169",
                              "geo": {
                                "lat": "-14.3990",
                                "lng": "-120.7677"
                              }
                            },
                            "phone": "586.493.6943 x140",
                            "website": "jacynthe.com",
                            "company": {
                              "name": "Abernathy Group",
                              "catchPhrase": "Implemented secondary concept",
                              "bs": "e-enable extensible e-tailers"
                            }
                          }

        valid, response = get_user_info(email)

        self.assertTrue(valid)

        self.assertEqual(response, expected_response)

    def test_get_user_info_invalid(self):
        email = 'sallve@esfoliante.nice'
        expected_response = {}

        valid, response = get_user_info(email)

        self.assertFalse(valid)

        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
