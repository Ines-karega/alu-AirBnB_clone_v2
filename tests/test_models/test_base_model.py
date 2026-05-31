#!/usr/bin/python3
"""Unit tests for BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os
import time


class TestBaseModelInstantiation(unittest.TestCase):
    """Tests for BaseModel instantiation."""

    def test_instance_created(self):
        """Test that a BaseModel instance is created."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_is_string(self):
        """Test that id is a string."""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)

    def test_id_unique(self):
        """Test that each instance has a unique id."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        obj = BaseModel()
        self.assertIsInstance(obj.updated_at, datetime)

    def test_created_at_equals_updated_at_on_creation(self):
        """Test that created_at and updated_at are close on creation."""
        obj = BaseModel()
        self.assertAlmostEqual(
            obj.created_at.timestamp(),
            obj.updated_at.timestamp(),
            delta=0.01
        )

    def test_str_representation(self):
        """Test the string representation of BaseModel."""
        obj = BaseModel()
        expected = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(str(obj), expected)

    def test_kwargs_instantiation(self):
        """Test instantiation with kwargs."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(obj.id, new_obj.id)
        self.assertEqual(obj.created_at, new_obj.created_at)
        self.assertEqual(obj.updated_at, new_obj.updated_at)

    def test_kwargs_no_class_attribute(self):
        """Test that __class__ key is not set as attribute."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertNotIn("__class__", new_obj.__dict__)

    def test_kwargs_dates_converted(self):
        """Test that date strings are converted to datetime objects."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)

    def test_no_args_creates_new_id(self):
        """Test that instantiation without args creates a new id."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_args_unused(self):
        """Test that args are not used."""
        obj = BaseModel("test", 1, 2)
        self.assertIsInstance(obj.id, str)


class TestBaseModelSave(unittest.TestCase):
    """Tests for BaseModel save method."""

    def test_save_updates_updated_at(self):
        """Test that save updates updated_at."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        time.sleep(0.05)
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_save_creates_file(self):
        """Test that save creates the JSON file."""
        obj = BaseModel()
        obj.save()
        self.assertTrue(os.path.exists("file.json"))

    def tearDown(self):
        """Remove file.json after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


class TestBaseModelToDict(unittest.TestCase):
    """Tests for BaseModel to_dict method."""

    def test_to_dict_returns_dict(self):
        """Test that to_dict returns a dictionary."""
        obj = BaseModel()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_has_class_key(self):
        """Test that to_dict result has __class__ key."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_to_dict_created_at_is_string(self):
        """Test that created_at is converted to string."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict["created_at"], str)

    def test_to_dict_updated_at_is_string(self):
        """Test that updated_at is converted to string."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_to_dict_created_at_format(self):
        """Test that created_at follows ISO format."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        try:
            datetime.strptime(obj_dict["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            self.fail("created_at is not in ISO format")

    def test_to_dict_contains_id(self):
        """Test that to_dict result contains id."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn("id", obj_dict)
        self.assertEqual(obj_dict["id"], obj.id)

    def test_to_dict_contains_all_keys(self):
        """Test that to_dict contains all instance attributes."""
        obj = BaseModel()
        obj.name = "Test"
        obj_dict = obj.to_dict()
        self.assertIn("name", obj_dict)

    def tearDown(self):
        """Remove file.json after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
