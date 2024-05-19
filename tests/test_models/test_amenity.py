#!/usr/bin/python3

""" Unittest for amenity.py """


import unittest
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up a new Amenity instance for testing"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after each test method"""
        del self.amenity

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test the Amenity-specific attributes"""
        self.assertEqual(self.amenity.name, "")

    def test_str_representation(self):
        """Test the string representation of the Amenity instance"""
        expected = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains all the correct keys"""
        amenity_dict = self.amenity.to_dict()
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('__class__', amenity_dict)

    def test_to_dict_contains_added_attributes(self):
        """Test to_dict() contains attributes added after initialization"""
        self.amenity.name = "Pool"
        amenity_dict = self.amenity.to_dict()
        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['name'], "Pool")

    def test_to_dict_values(self):
        """Test the values in the dictionary returned by to_dict()"""
        self.amenity.name = "Pool"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'], self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict['name'], "Pool")

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        self.amenity.name = "Pool"
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertEqual(new_amenity.id, self.amenity.id)
        self.assertEqual(new_amenity.created_at, self.amenity.created_at)
        self.assertEqual(new_amenity.updated_at, self.amenity.updated_at)
        self.assertEqual(new_amenity.name, "Pool")


if __name__ == '__main__':
    unittest.main()
