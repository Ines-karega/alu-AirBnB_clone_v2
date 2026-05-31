#!/usr/bin/python3
"""Unit tests for Place class."""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlaceInstantiation(unittest.TestCase):
    """Tests for Place instantiation."""

    def test_place_is_base_model(self):
        """Test that Place inherits from BaseModel."""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_instance(self):
        """Test that Place instantiates correctly."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_city_id_default(self):
        """Test that city_id default is empty string."""
        self.assertEqual(Place.city_id, "")

    def test_user_id_default(self):
        """Test that user_id default is empty string."""
        self.assertEqual(Place.user_id, "")

    def test_name_default(self):
        """Test that name default is empty string."""
        self.assertEqual(Place.name, "")

    def test_description_default(self):
        """Test that description default is empty string."""
        self.assertEqual(Place.description, "")

    def test_number_rooms_default(self):
        """Test that number_rooms default is 0."""
        self.assertEqual(Place.number_rooms, 0)

    def test_number_bathrooms_default(self):
        """Test that number_bathrooms default is 0."""
        self.assertEqual(Place.number_bathrooms, 0)

    def test_max_guest_default(self):
        """Test that max_guest default is 0."""
        self.assertEqual(Place.max_guest, 0)

    def test_price_by_night_default(self):
        """Test that price_by_night default is 0."""
        self.assertEqual(Place.price_by_night, 0)

    def test_latitude_default(self):
        """Test that latitude default is 0.0."""
        self.assertEqual(Place.latitude, 0.0)

    def test_longitude_default(self):
        """Test that longitude default is 0.0."""
        self.assertEqual(Place.longitude, 0.0)

    def test_amenity_ids_default(self):
        """Test that amenity_ids default is empty list."""
        self.assertEqual(Place.amenity_ids, [])

    def test_to_dict_contains_class(self):
        """Test that to_dict contains __class__ = Place."""
        place = Place()
        d = place.to_dict()
        self.assertEqual(d["__class__"], "Place")

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
