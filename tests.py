import unittest
import pytest
import main
from main import save_user, load_users, sign_in, create_new_user, populate_userTBU, update_userJson, createJSON, create_password, timeclock, create_task

def test_save_user():
    assert save_user(self, mock_exists, mock_open)
    user = User(name="SPe")

def test_sign_in(self, mock_input):
    user = User()
    result = sign_in(user)
    self.assertIsNotNone(result)
    self.assertEqual(user.name, "Daniel")
    self.assertTrue(user.is_admin)

def test_incorrect_password(self, mock_input):
        user = User()
        result = sign_in(user)
        self.assertIsNone(result)

def test_user_not_found(self, mock_input):
        user = User()
        result = sign_in(user)
        self.assertIsNone(result)

def test_create_new_user():
    ...

def test_populate_userTBU():
    ...

def test_update_userJSON():
    ...

def creat_password():
    ...

