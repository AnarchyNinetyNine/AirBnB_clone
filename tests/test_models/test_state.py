#!/usr/bin/python3

""" Unittest for state.py """


import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """Test cases for the State class"""

    def setUp(self):
        """Set up a new State instance for testing"""
        self.state = State()

    def tearDown(self):
        """Clean up after each test method"""
        del self.state

    def test_inheritance(self):
        """Test that State inherits from BaseModel"""
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test the State-specific attributes"""
        self.assertEqual(self.state.name, "")

    def test_str_representation(self):
        """Test the string representation of the State instance"""
        expected = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains all the correct keys"""
        state_dict = self.state.to_dict()
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('__class__', state_dict)

    def test_to_dict_contains_added_attributes(self):
        """Test that to_dict() contains attributes added after initialization"""
        self.state.name = "California"
        state_dict = self.state.to_dict()
        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['name'], "California")

    def test_to_dict_values(self):
        """Test the values in the dictionary returned by to_dict()"""
        self.state.name = "California"
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['created_at'], self.state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'], self.state.updated_at.isoformat())
        self.assertEqual(state_dict['name'], "California")

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        self.state.name = "California"
        state_dict = self.state.to_dict()
        new_state = State(**state_dict)
        self.assertEqual(new_state.id, self.state.id)
        self.assertEqual(new_state.created_at, self.state.created_at)
        self.assertEqual(new_state.updated_at, self.state.updated_at)
        self.assertEqual(new_state.name, "California")


if __name__ == '__main__':
    unittest.main()
