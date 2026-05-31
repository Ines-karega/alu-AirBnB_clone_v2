#!/usr/bin/python3
"""Unit tests for Amenity class."""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityInstantiation(unittest.TestCase):
    """Tests for Amenity instantiation."""

    def test_amenity_is_base_model(self):
        """Test that Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_instance(self):
        """Test that Amenity instantiates correctly."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_name_default(self):
        """Test that name default is empty string."""
        self.assertEqual(Amenity.name, "")

    def test_name_is_str(self):
        """Test that name is a string."""
        self.assertIsInstance(Amenity.name, str)

    def test_to_dict_contains_class(self):
        """Test that to_dict contains __class__ = Amenity."""
        amenity = Amenity()
        d = amenity.to_dict()
        self.assertEqual(d["__class__"], "Amenity")

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
