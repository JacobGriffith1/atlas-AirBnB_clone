#!/usr/bin/python3
""" unittest for review.py """
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """ test cases for review class """

    def test_review_intialization(self):
        """ test initialization of review attributes """
        self.review = Review()

        # check that all attributes are initialized to empty strings
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_attributes(self):
        """ test assignment of review attributes """
        self.review = Review()

        # assign values to attributes
        self.review.place_id = "1234"
        self.review.user_id = "5678"
        self.review.text = "This is a review!"

        # check that attributes hold assigned values
        self.assertEqual(self.review.place_id, "1234")
        self.assertEqual(self.review.user_id, "5678")
        self.assertEqual(self.review.text, "This is a review!")

if __name__ == '__main__':
    unittest.main()
