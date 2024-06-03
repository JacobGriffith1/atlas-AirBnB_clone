#!/usr/bin/python3
""" unittest file for city.py """
import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """ test cases for city class """

    def test_city_intialization(self):
        """ test initialization of city attributes """
        self.city = City()

        # check that attributes are intialized to empty strings
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_attributes(self):
        """ test assignment of city attributes """
        self.city = City()

        # assign values to attributes
        self.city.state_id = "1234"
        self.city.name = "Tulsa"
        # check that attributes hold assigned values
        self.assertEqual(self.city.state_id, "1234")
        self.assertEqual(self.city.name, "Tulsa")

if __name__ == '__main__':
    unittest.main()
