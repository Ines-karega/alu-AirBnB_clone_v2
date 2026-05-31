#!/usr/bin/python3
"""Unit tests for City class."""
import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCityInstantiation(unittest.TestCase):
    """Tests for City instantiation."""

    def test_city_is_base_model(self):
        """Test that City inherits from BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_instance(self):
        """Test that City instantiates correctly."""
        city = City()
        self.assertIsInstance(city, City)

    def test_state_id_default(self):
        """Test that state_id default is empty string."""
        self.assertEqual(City.state_id, "")

    def test_name_default(self):
        """Test that name default is empty string."""
        self.assertEqual(City.name, "")

    def test_state_id_is_str(self):
        """Test that state_id is a string."""
        self.assertIsInstance(City.state_id, str)

    def test_name_is_str(self):
        """Test that name is a string."""
        self.assertIsInstance(City.name, str)

    def test_to_dict_contains_class(self):
        """Test that to_dict contains __class__ = City."""
        city = City()
        d = city.to_dict()
        self.assertEqual(d["__class__"], "City")

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
