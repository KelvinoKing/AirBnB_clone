#!/usr/bin/python3
"""Unittest for base_model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class to test BaseModel class
    """

    def test_class_instance(self):
        """test if the obj is an instance of object class
        """

        obj = BaseModel()
        self.assertIsInstance(obj, object)

    def test_class_attribute_id(self):
        """test whether the id is a string
        """
        my_obj = BaseModel()
        self.assertIsInstance(my_obj.id, str)

    def test_obj_equal(self):
        """test whether two objs are equal
        """

        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1, obj2)

    def test_class_attribure_number(self):
        """Test whether my_number is int
        """

        obj = BaseModel()
        self.assertIsInstance(obj.update_at, int)

    def test_class_attribute_name(self):
        """Test if name attr is str
        """

        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
