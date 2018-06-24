"""
Tests for DictStorage.
"""

import unittest

from storages.dict_storage.dict_storage import DictStorage
from storages.dict_storage.exceptions import KeyAlreadyExists, KeyDoesntExist


class TestDictStorage(unittest.TestCase):

    def setUp(self):
        self.dict_storage = DictStorage()

    def test_save(self):
        """
        Test the save method.
        """
        self.dict_storage.save("test_key", "test_value")
        self.assertIn("test_key", self.dict_storage._internal_dict)
        self.assertEqual("test_value", self.dict_storage._internal_dict.get("test_key"))

        with self.assertRaises(KeyAlreadyExists):
            self.dict_storage.save("test_key", "another_test_value")

        self.dict_storage.save("test_key", "another_test_value_2", override=True)
        self.assertIn("test_key", self.dict_storage._internal_dict)
        self.assertEqual("another_test_value_2", self.dict_storage._internal_dict.get("test_key"))

    def test_load(self):
        """
        Test the load method.
        """
        self.dict_storage._internal_dict["test_key"] = "test_value"
        self.assertEqual(self.dict_storage.load("test_key"), "test_value")

        with self.assertRaises(KeyDoesntExist):
            self.dict_storage.load("bad_test_key")

    def test_delete(self):
        """
        Test the delete method.
        """
        with self.assertRaises(KeyDoesntExist):
            self.dict_storage.delete("test_key")

        self.assertNotIn("test_key", self.dict_storage._internal_dict)
        self.dict_storage._internal_dict["test_key"] = "test_value"
        self.assertIn("test_key", self.dict_storage._internal_dict)
        self.dict_storage.delete("test_key")
        self.assertNotIn("test_key", self.dict_storage._internal_dict)
