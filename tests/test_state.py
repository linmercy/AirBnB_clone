#!/usr/bin/python3
"""Test State Module"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """TestState class"""

    def test_attributes(self):
        """Test attributes"""
        state = State()
        self.assertTrue(hasattr(state, "name"))

