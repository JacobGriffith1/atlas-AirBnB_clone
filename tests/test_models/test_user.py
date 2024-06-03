#!/usr/bin/python3
""" unittest file for user.py """
import unittest
from models.user import User


class Test_User(unittest.TestCase):
    """ test cases for User class """

    def test_user_initialization(self):
        """ test initialization of user attributes """
        self.user = User()

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_attributes(self):
        """ check that attributes are correctly assigned """
        self.user = User()

        # assign values to attributes
        self.user.email = "test@user.com"
        self.user.password = "password"
        self.user.first_name = "First"
        self.user.last_name = "Last"
        # check that attributes hold assigned values
        self.assertEqual(self.user.email, "test@user.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "First")
        self.assertEqual(self.user.last_name, "Last")

if __name__ == '__main__':
    unittest.main()
