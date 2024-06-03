#!/usr/bin/python3
""" unittest file for state.py """
import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """ test cases for state class"""

    def test_state_initialization(self):
        """ test initialization of state attributes """
        self.state = State()

        # check that name attribute is intialized
        self.assertEqual(self.state.name, "")

    def test_state_attributes(self):
        """ test assignment of state attributes"""
        self.state = State()

        # assign a value to name attribute
        self.state.name = "Oklahoma"
        # check that name holds the correct value
        self.assertEqual(self.state.name, "Oklahoma")

if __name__ == '__main__':
    unittest.main()
