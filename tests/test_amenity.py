#!/usr/bin/python3
"""Test Amenity Module"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """TestAmenity class"""

    def test_attributes(self):
        """Test attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

