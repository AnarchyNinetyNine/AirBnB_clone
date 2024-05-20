#!/usr/bin/python3

""" Unittest for file_storage.py """


import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up a new FileStorage instance for testing"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after each test method"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary"""
        self.assertEqual(type(self.storage.all()), dict)

    def test_new_adds_object(self):
        """Test that new() correctly adds an object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that save() correctly saves objects to file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r') as file:
            content = json.load(file)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, content)

    def test_reload(self):
        """Test that reload() correctly loads objects from file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()
