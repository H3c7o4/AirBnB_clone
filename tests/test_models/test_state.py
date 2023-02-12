#!/usr/bin/python3


"""Unittest User"""


import unittest
import os
from models.user import User
from models.base_model import BaseModel


class test_Amenity(unittest.TestCase):

    @classmethod
    def setup(self):
        self.state1 = State()
        self.state1.name = "Monte Carlo"

    @classmethod
    def tearDown(self):
        del self.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_to_dict(self):
        self.assertEqual("to_dict" in dir(self.state1), True)

    def test_functions(self):
        self.assertIsNotNone(State.__doc__)

    def save_test(self):
        self.state1.save()
        self.assertNotEqual(self.state1.created_at,
                            self.state1.updated_at)

    def test_subclass(self):
        self.assertTrue(issubclass(self.state1.__class__.BaseModel), True)

    def test_attributes(self):
        self.assertTrue("name" in self.state1.__dict__)
        self.assertTrue("created_at" in self.state1.__dict__)
        self.assertTrue("updated_at" in self.state1.__dict__)
        self.assertTrue("id" in self.state1.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.state1.name), str)

if __name__ == "__main__":
    unittest.main()
