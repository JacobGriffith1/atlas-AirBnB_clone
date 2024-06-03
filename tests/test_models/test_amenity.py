#!/usr/bin/python3
""" unittest for amenity.py """
import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ test cases for amenity class """

    def test_amenity_initialization(self):
        """ test initialization of amenity attributes """
        self.amenity = Amenity()

        # check that all attributes are initialized to empty strings
        self.assertEqual(self.amenity.name, "")

    def test_amenity_attributes(self):
        """ tests assignment of amenity attributes """
        self.amenity = Amenity()

        # assign value to attribute
        self.amenity.name = "wifi"
        # check that attribute holds assigned value
        self.assertEqual(self.amenity.name, "wifi")

if __name__ == '__main__':
    unittest.main()
