#!/usr/bin/python3

""" Ynittest for review.py """


import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up a new Review instance for testing"""
        self.review = Review()

    def tearDown(self):
        """Clean up after each test method"""
        del self.review

    def test_inheritance(self):
        """Test that Review inherits from BaseModel"""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test the Review-specific attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_str_representation(self):
        """Test the string representation of the Review instance"""
        expected = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute"""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains all the correct keys"""
        review_dict = self.review.to_dict()
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('__class__', review_dict)

    def test_to_dict_contains_added_attributes(self):
        """Test that to_dict() contains attributes added after initialization"""
        self.review.text = "Great place!"
        review_dict = self.review.to_dict()
        self.assertIn('text', review_dict)
        self.assertEqual(review_dict['text'], "Great place!")

    def test_to_dict_values(self):
        """Test the values in the dictionary returned by to_dict()"""
        self.review.text = "Great place!"
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertEqual(review_dict['created_at'], self.review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'], self.review.updated_at.isoformat())
        self.assertEqual(review_dict['text'], "Great place!")

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs"""
        self.review.text = "Great place!"
        review_dict = self.review.to_dict()
        new_review = Review(**review_dict)
        self.assertEqual(new_review.id, self.review.id)
        self.assertEqual(new_review.created_at, self.review.created_at)
        self.assertEqual(new_review.updated_at, self.review.updated_at)
        self.assertEqual(new_review.text, "Great place!")


if __name__ == '__main__':
    unittest.main()
