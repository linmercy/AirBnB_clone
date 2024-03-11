#!/usr/bin/python3
"""Test City Module"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """TestCity class"""

    def test_attributes(self):
        """Test attributes"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

