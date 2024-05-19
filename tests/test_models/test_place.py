#!/usr/bin/python3

""" Unittest for place.py """


import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up a new Place instance for testing"""
        self.place = Place()

    def tearDown(self):
        """Clean up after each test method"""
        del self.place

    def test_inheritance(self):
        """Test that Place inherits from BaseModel"""
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test the Place-specific attributes"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_str_representation(self):
        """Test the string representation of the Place instance"""
        expected = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute"""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains all the correct keys"""
        place_dict = self.place.to_dict()
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('__class__', place_dict)

    def test_to_dict_contains_added_attributes(self):
        """Test that to_dict() contains attributes added after initialization"""
        self.place.name = "My Place"
        place_dict = self.place.to_dict()
        self.assertIn('name', place_dict)
        self.assertEqual(place_dict['name'], "My Place")

    def test_to_dict_values(self):
        """Test the values in the dictionary returned by to_dict()"""
        self.place.name = "My Place"
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['created_at'], self.place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'], self.place.updated_at.isoformat())
        self.assertEqual(place_dict['name'], "My Place")

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        self.place.name = "My Place"
        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)
        self.assertEqual(new_place.id, self.place.id)
        self.assertEqual(new_place.created_at, self.place.created_at)
        self.assertEqual(new_place.updated_at, self.place.updated_at)
        self.assertEqual(new_place.name, "My Place")


if __name__ == '__main__':
    unittest.main()
