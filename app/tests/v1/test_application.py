import unittest
from flask import json, current_app
from app import create_app


class TestClient(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def teardown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_all_products_endpoint(self):
        response = self.client.get('api/v1/products')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
