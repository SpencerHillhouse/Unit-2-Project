import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from main import User, load_users, sign_in, create_new_user, create_password, admin_view_tasks

class TestStuff(unittest.TestCase):
    @patch("builtins.input", side_effect=["Admin","admin"])
    def test_sign_in(self, mock_input):
        user = User
        result = sign_in(user)
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Admin")
        self.assertTrue(result["is_admin"])
    
    @patch('builtins.input', side_effect=["Admin", "wrongpassword"])
    def test_incorrect_password(self, mock_input):
        user = User
        result = sign_in(user)
        self.assertIsNone(result)
    
    
    @patch("builtins.input", side_effect=["", ""])
    def test_user_not_found(self, mock_input):
            user = User
            result = sign_in(user)
            self.assertIsNone(result)
            
    @patch("builtins.input", side_effect=["Y","Quan", "1234567", "quan@gmail.com"])
    def test_create_new_user(self, mock_input):
         result = create_new_user()
         self.assertEqual(result.is_admin, True)
         self.assertEqual(result.name, "Quan")
         self.assertEqual(result.phone_number, "1234567")
         self.assertEqual(result.email, "quan@gmail.com")
                         
    @patch('builtins.input', side_effect=["password1", "password1"])
    def test_successful_password_creation(self, mock_input):
        user = User
        create_password(user)
        users = load_users()
        quan = next((u for u in users if u['name'] == 'Quan'), None)
        self.assertIsNotNone(quan)
        self.assertEqual('password1', 'password1')
        self.assertFalse(user.is_first_login)

    @patch("builtins.input", side_effect=["alskdfj", []])
    def test_admin_view_task(self, mock_input):
         result = admin_view_tasks()
         self.assertEqual(result, None)