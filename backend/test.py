import unittest
import json

from .apis_book_a_meal import app
from models import DbUsers, DbCaterers


class TestAPIs(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        # user_db = DbUsers()
        # caterer_db = DbCaterers()

    def test_successful_registration(self):
        input_data = dict(category='user', email='default@gmail.com', username='default', password='12345',
                          confirm_password='12345', address='address1')
        expected_reponse_message = '{} successfully signed up.'.format(input_data['username'])
        get_response = self.tester.post('/auth/signup', content_type="application/json", data=json.dumps(input_data))

        self.assertEqual(get_response.status_code, 201)
        self.assertEqual(get_response.data['message'], expected_reponse_message)


if __name__ == '__main__':
    unittest.main()