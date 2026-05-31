#!/usr/bin/python3
"""Unit tests for FileStorage class."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorageInstantiation(unittest.TestCase):
    """Tests for FileStorage instantiation."""

    def test_file_storage_instantiation(self):
        """Test that FileStorage instantiates correctly."""
        self.assertIsInstance(FileStorage(), FileStorage)

    def test_storage_is_file_storage(self):
        """Test that storage is an instance of FileStorage."""
        self.assertIsInstance(storage, FileStorage)


class TestFileStorageAll(unittest.TestCase):
    """Tests for FileStorage all method."""

    def test_all_returns_dict(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_all_returns_same_dict(self):
        """Test that all returns the same dict object each call."""
        self.assertIs(storage.all(), storage.all())


class TestFileStorageNew(unittest.TestCase):
    """Tests for FileStorage new method."""

    def test_new_adds_to_objects(self):
        """Test that new adds an object to __objects."""
        obj = BaseModel()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


class TestFileStorageSave(unittest.TestCase):
    """Tests for FileStorage save method."""

    def test_save_creates_file(self):
        """Test that save creates the JSON file."""
        obj = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_file_contains_object(self):
        """Test that the saved file contains the object."""
        obj = BaseModel()
        storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, data)

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


class TestFileStorageReload(unittest.TestCase):
    """Tests for FileStorage reload method."""

    def test_reload_loads_objects(self):
        """Test that reload loads objects from the file."""
        obj = BaseModel()
        obj.save()
        storage.reload()
        key = "BaseModel.{}".format(obj.id)
        self.assertIn(key, storage.all())

    def test_reload_no_file_no_error(self):
        """Test that reload raises no error if file doesn't exist."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            storage.reload()
        except Exception as e:
            self.fail("reload raised exception: {}".format(e))

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
