#!/usr/bin/python3
"""Test Review Module"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """TestReview class"""

    def test_attributes(self):
        """Test attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

