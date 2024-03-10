#!/usr/bin/python3
"""Unit tests for BaseModel class."""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test environment."""
        del self.model

    def test_instance_attributes(self):
        """Test instance attributes."""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        """Test id generation."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_updated_at(self):
        """Test created_at and updated_at attributes."""
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_method(self):
        """Test save method."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_str_method(self):
        """Test __str__ method."""
        expected = "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__
        )
        self.assertEqual(str(self.model), expected)


if __name__ == '__main__':
    unittest.main()
