import unittest
import json
from Application import app, schemas as sc
from flask import jsonify
from flask_login import login_user

class BookAPITests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_book(self):
        data = {
            "title": "The Hitchhiker's Guide to the Galaxy",
            "author": "Douglas Adams",
            "ISBN": "9780345391827",
            "price": 12.99,
            "quantity": 5
        }

        response = self.app.post('/add_book', json=data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "Book added successfully")

    def test_get_books(self):
        response = self.app.get('/get_books')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data['books'], list)

    def test_get_book_by_isbn(self):
        isbn = "9780345391827"
        response = self.app.get(f'/get_book/{isbn}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data['book'], dict)

    def test_update_book(self):
        isbn = "9780345391827"
        data = {
            "title": "The Hitchhiker's Guide to the Galaxy",
            "author": "Douglas Adams",
            "ISBN": "9780345391827",
            "price": 14.99,
            "quantity": 10
        }

        response = self.app.put(f'/update_book/{isbn}', json=data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "Book updated successfully")

    def test_delete_book(self):
        isbn = "9780345391827"
        response = self.app.delete(f'/delete_book/{isbn}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "Book deleted successfully")




class UserAPITests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_register(self):
        data = {
            "username": "test_user",
            "password": "test_password",
            "email": "test@example.com"
        }

        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "user added successfully")

    def test_login(self):
        data = {
            "username": "test_user",
            "password": "test_password",
        }

        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "login success")

    def test_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['message'], "user logged out.")

if __name__ == '__main__':
    unittest.main()