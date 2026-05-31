#!/usr/bin/python3
"""Unit tests for State class."""
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestStateInstantiation(unittest.TestCase):
    """Tests for State instantiation."""

    def test_state_is_base_model(self):
        """Test that State inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_instance(self):
        """Test that State instantiates correctly."""
        state = State()
        self.assertIsInstance(state, State)

    def test_name_default(self):
        """Test that name default is empty string."""
        self.assertEqual(State.name, "")

    def test_name_is_str(self):
        """Test that name is a string."""
        self.assertIsInstance(State.name, str)

    def test_to_dict_contains_class(self):
        """Test that to_dict contains __class__ = State."""
        state = State()
        d = state.to_dict()
        self.assertEqual(d["__class__"], "State")

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
