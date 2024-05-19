#!/usr/bin/python3

""" Unittest for user.py """


import unittest
from datetime import datetime
import sys
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    """Test cases for the User class"""

    def setUp(self):
        """Set up a new User instance for testing"""
        self.user = User()

    def tearDown(self):
        """Clean up after each test method"""
        del self.user

    def test_inheritance(self):
        """Test that User inherits from BaseModel"""
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test the User-specific attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_str_representation(self):
        """Test the string representation of the User instance"""
        expected = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains all the correct keys"""
        user_dict = self.user.to_dict()
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)

    def test_to_dict_contains_added_attributes(self):
        """Test that to_dict() contains attributes added after initialization"""
        self.user.email = "test@example.com"
        self.user.password = "test1234"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        user_dict = self.user.to_dict()
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)

    def test_to_dict_values(self):
        """Test the values in the dictionary returned by to_dict()"""
        self.user.email = "test@example.com"
        self.user.password = "test1234"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'], self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], self.user.updated_at.isoformat())
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "test1234")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        self.user.email = "test@example.com"
        self.user.password = "test1234"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        user_dict = self.user.to_dict()
        new_user = User(**user_dict)
        self.assertEqual(new_user.id, self.user.id)
        self.assertEqual(new_user.created_at, self.user.created_at)
        self.assertEqual(new_user.updated_at, self.user.updated_at)
        self.assertEqual(new_user.email, "test@example.com")
        self.assertEqual(new_user.password, "test1234")
        self.assertEqual(new_user.first_name, "John")
        self.assertEqual(new_user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
