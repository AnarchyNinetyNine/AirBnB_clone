#!/usr/bin/python3

""" Unittest for city.py """


import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up a new City instance for testing"""
        self.city = City()

    def tearDown(self):
        """Clean up after each test method"""
        del self.city

    def test_inheritance(self):
        """Test that City inherits from BaseModel"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test the City-specific attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_str_representation(self):
        """Test the string representation of the City instance"""
        expected = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains all the correct keys"""
        city_dict = self.city.to_dict()
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('__class__', city_dict)

    def test_to_dict_contains_added_attributes(self):
        """Test that to_dict() contains attributes added after initialization"""
        self.city.state_id = "1234"
        self.city.name = "San Francisco"
        city_dict = self.city.to_dict()
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['state_id'], "1234")
        self.assertEqual(city_dict['name'], "San Francisco")

    def test_to_dict_values(self):
        """Test the values in the dictionary returned by to_dict()"""
        self.city.state_id = "1234"
        self.city.name = "San Francisco"
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['created_at'], self.city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], self.city.updated_at.isoformat())
        self.assertEqual(city_dict['state_id'], "1234")
        self.assertEqual(city_dict['name'], "San Francisco")

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        self.city.state_id = "1234"
        self.city.name = "San Francisco"
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertEqual(new_city.id, self.city.id)
        self.assertEqual(new_city.created_at, self.city.created_at)
        self.assertEqual(new_city.updated_at, self.city.updated_at)
        self.assertEqual(new_city.state_id, "1234")
        self.assertEqual(new_city.name, "San Francisco")


if __name__ == '__main__':
    unittest.main()
