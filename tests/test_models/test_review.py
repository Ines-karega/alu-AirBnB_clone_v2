#!/usr/bin/python3
"""Unit tests for Review class."""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReviewInstantiation(unittest.TestCase):
    """Tests for Review instantiation."""

    def test_review_is_base_model(self):
        """Test that Review inherits from BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_instance(self):
        """Test that Review instantiates correctly."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_place_id_default(self):
        """Test that place_id default is empty string."""
        self.assertEqual(Review.place_id, "")

    def test_user_id_default(self):
        """Test that user_id default is empty string."""
        self.assertEqual(Review.user_id, "")

    def test_text_default(self):
        """Test that text default is empty string."""
        self.assertEqual(Review.text, "")

    def test_place_id_is_str(self):
        """Test that place_id is a string."""
        self.assertIsInstance(Review.place_id, str)

    def test_user_id_is_str(self):
        """Test that user_id is a string."""
        self.assertIsInstance(Review.user_id, str)

    def test_text_is_str(self):
        """Test that text is a string."""
        self.assertIsInstance(Review.text, str)

    def test_to_dict_contains_class(self):
        """Test that to_dict contains __class__ = Review."""
        review = Review()
        d = review.to_dict()
        self.assertEqual(d["__class__"], "Review")

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
