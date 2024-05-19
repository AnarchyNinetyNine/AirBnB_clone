#!/usr/bin/python3

""" Unittest for base_model.py """


import sys
import os
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up a new BaseModel instance for testing"""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after each test method"""
        del self.model

    def test_id_is_unique(self):
        """Test that each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)
        del model2

    def test_id_is_string(self):
        """Test that the id is a string"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of the model"""
        expected = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains all the correct keys"""
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_contains_added_attributes(self):
        """Test that to_dict() contains attributes added after initialization"""
        self.model.name = "Test"
        self.model.number = 42
        model_dict = self.model.to_dict()
        self.assertIn('name', model_dict)
        self.assertIn('number', model_dict)

    def test_to_dict_values(self):
        """Test the values in the dictionary returned by to_dict()"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)


if __name__ == '__main__':
    unittest.main()
