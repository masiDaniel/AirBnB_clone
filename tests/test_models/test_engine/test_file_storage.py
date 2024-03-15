#!usr/bin/python3
"""Tests for FileStorage class"""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def test_all(self):
        """Test all method"""
        self.assertEqual(type(storage.all()), dict)
        obj = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        storage.new(obj)
        storage.new(obj2)
        storage.new(obj3)
        key = obj.__class__.__name__ + "." + obj.id
        self.assertTrue(key in storage.all())
        key = obj2.__class__.__name__ + "." + obj2.id
        self.assertTrue(key in storage.all())
        key = obj3.__class__.__name__ + "." + obj3.id
        self.assertTrue(key in storage.all())

    def test_new(self):
        """Tests new method"""
        base = BaseModel()
        storage.new(base)
        key = base.__class__.__name__ + "." + base.id
        self.assertEqual(storage.all()[key], base)

    def test_save(self):
        """ Tests the FileStorage save method """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Test if storage file is successfully loaded to __objects """
        base = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(base.to_dict()['id'], loaded.to_dict()['id'])

    def test_file_path(self):
        """Test file_path """
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_objects(self):
        """Test objects """
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_file_path_value(self):
        """Test file_path attribute value"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_file_path_private(self):
        """Test if file_path attribute is private"""
        with self.assertRaises(AttributeError):
            print(FileStorage.__file_path)

    def test_file_storage_reload(self):
        """Test reload method"""
        storage.reload()
        self.assertEqual(type(storage.all()), dict)

    def test_file_storage_save(self):
        """Test save method"""
        storage.save()
        self.assertEqual(type(storage.all()), dict)

# import unittest
# from unittest.mock import patch
# from io import StringIO
# from console import HBNBCommand
# from models import storage
# from models.base_model import BaseModel
# from models.user import User


# class TestFileStorage(unittest.TestCase):
#     def setUp(self):
#         self.storage = storage
#         self.base_model = BaseModel()
#         self.user = User()

#     def tearDown(self):
#         self.storage.reload()

#     def test_all(self):
#         self.assertIsInstance(self.storage.all(), dict)
#         self.assertIsInstance(self.storage.all(BaseModel), dict)
#         self.assertIsInstance(self.storage.all(User), dict)

#     def test_new(self):
#         self.storage.new(self.base_model)
#         self.assertIn("BaseModel.{}".format(
#             self.base_model.id), self.storage.all())
#         self.storage.new(self.user)
#         self.assertIn("User.{}".format(self.user.id), self.storage.all())

#     def test_save(self):
#         self.storage.new(self.base_model)
#         self.storage.new(self.user)
#         self.storage.save()
#         with open(self.storage._FileStorage__file_path, "r") as f:
#             data = f.read()
#             self.assertIn("BaseModel.{}".format(self.base_model.id), data)
#             self.assertIn("User.{}".format(self.user.id), data)

#     def test_reload(self):
#         self.storage.new(self.base_model)
#         self.storage.new(self.user)
#         self.storage.save()
#         self.storage.reload()
#         self.assertIn("BaseModel.{}".format(
#             self.base_model.id), self.storage.all())
#         self.assertIn("User.{}".format(self.user.id), self.storage.all())