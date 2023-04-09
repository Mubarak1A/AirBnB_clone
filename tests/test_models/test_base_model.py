#!/usr/bin/python3
""" Module to test BaseModel class attributes and functions """
import unittest
from os import path
from datetime import datetime
from AirBnB_clone.tests import BaseModel



class test_BaseModel(unittest.TestCase):
    """ Test class for all BaseModel test functions """

    def setUp(self):
        """ to initialize instance of object """
        self.b1 = BaseModel()

    def test_attr_types(self):
        """ function to test the datatypes of all attributes """
        self.assertIsInstance(self.b1, BaseModel)
        self.assertIsInstance(self.b1.id, str)
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
