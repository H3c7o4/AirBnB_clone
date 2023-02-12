#!/usr/bin/python3


"""Unittest User"""


import unittest
import os
from models.user import User
from models.base_model import BaseModel


class test_Amenity(unittest.TestCase):

        @classmethod
        def setup(self):
            self.review1 = Review()
            self.review1.user_id = "Alan"
            self.review1.place_id = "Klein"
            self.review1.text = "Love You"

        @classmethod
        def tearDown(self):
            del self.review1
            try:
                os.remove("file.json")
            except FileNotFoundError:
                pass

        def test_to_dict(self):
            self.assertEqual("to_dict" in dir(self.review1), True)

        def test_functions(self):
            self.assertIsNotNone(Review.__doc__)

        def save_test(self):
            self.review1.save()
            self.assertNotEqual(self.review1.created_at,
                                self.review1.updated_at)

        def test_subclass(self):
            self.assertTrue(issubclass(self.review1.__class__.BaseModel), True)

        def test_attributes(self):
            self.assertTrue("created_at" in self.review1.__dict__)
            self.assertTrue("updated_at" in self.review1.__dict__)
            self.assertTrue("user_id" in self.review1.__dict__)
            self.assertTrue("placd_id" in self.review1.__dict__)
            self.assertTrue("text" in self.review1.__dict__)
            self.assertTrue("id" in self.review1.__dict__)

        def test_strings(self):
            self.assertEqual(type(self.review1.text), str)
            self.assertEqual(type(self.review1.place_id), str)
            self.assertEqual(type(self.review1.user_id), str)

if __name__ == "__main__":
    unittest.main()
