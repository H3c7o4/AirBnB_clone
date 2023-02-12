#!/usr/bin/python3


"""Unittest User"""


import unittest
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class test_filestore(unittest.TestCase):
    """test file_storage"""
    @classmethod
    def setup(self):
        self.review1 = Review()
        self.review1.user_id = "Tidus"
        self.review1.place_id = "Zanarkan"
        self.review1.text = "See you a next time"

    @classmethod
    def tearDown(self):
        del self.review1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_new(self):
        file1 = FileStorage()
        inst_dic = file1.all()
        tidus = User()
        tidus.id = 999999
        tidus.name = "Tidus"
        file1.new(tidus)
        key = tidu.__class__.__name__ + "." + str(tidus.id)
        self.assertIsNotNone(inst_dic[key])

    def test_all(self):
        file2 = FileStorage()
        instances_dic = file2.all()
        self.assertIsNotNone(inst_dic)
        self.assertEqual(type(inst_dic), dict)
        self.assertIs(inst_dic, file2._FileStorage__objects)

    def test_reload(self):
        file3 = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", mode="w") as f:
            for n in r:
                self.assertEqual(n, "{}")
        self.assertIs(file3.reload(), None)

if __name__ == "__main__":
    unittest.main()
