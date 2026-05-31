#!/usr/bin/python3
"""Unit tests for User class."""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUserInstantiation(unittest.TestCase):
    """Tests for User instantiation."""

    def test_user_is_base_model(self):
        """Test that User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_instance(self):
        """Test that User instantiates correctly."""
        user = User()
        self.assertIsInstance(user, User)

    def test_email_default(self):
        """Test that email default is empty string."""
        self.assertEqual(User.email, "")

    def test_password_default(self):
        """Test that password default is empty string."""
        self.assertEqual(User.password, "")

    def test_first_name_default(self):
        """Test that first_name default is empty string."""
        self.assertEqual(User.first_name, "")

    def test_last_name_default(self):
        """Test that last_name default is empty string."""
        self.assertEqual(User.last_name, "")

    def test_email_is_str(self):
        """Test that email is a string."""
        self.assertIsInstance(User.email, str)

    def test_password_is_str(self):
        """Test that password is a string."""
        self.assertIsInstance(User.password, str)

    def test_first_name_is_str(self):
        """Test that first_name is a string."""
        self.assertIsInstance(User.first_name, str)

    def test_last_name_is_str(self):
        """Test that last_name is a string."""
        self.assertIsInstance(User.last_name, str)

    def test_to_dict_contains_class(self):
        """Test that to_dict contains __class__ = User."""
        user = User()
        d = user.to_dict()
        self.assertEqual(d["__class__"], "User")

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
