#!/usr/bin/python3
"""import all dependencies to support tests
"""
import unittest
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class to handle all test cases of FileStorage class
    """

    def setUp(self):
        """Create an instance of FileStorage and
        reset the __objects dictionary"""

        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def test_all(self):
        """Test the 'all' method"""

        new_user = User()
        self.storage.new(new_user)
        objects = self.storage.all()
        self.assertIn('User.{}'.format(new_user.id), objects)

    def test_new(self):
        """Test the 'new' method"""

        new_user = User()
        self.storage.new(new_user)
        objects = self.storage.all()
        self.assertIn('User.{}'.format(new_user.id), objects)

    def test_save_and_reload(self):
        """Test the 'save' and 'reload' methods"""

        new_user = User()
        self.storage.new(new_user)

        # Save the data to file and reload it
        self.storage.save()
        self.storage.reload()

        # Check if the reloaded object is in the 'all' result
        objects = self.storage.all()
        self.assertIn('User.{}'.format(new_user.id), objects)


if __name__ == '__main__':
    unittest.main()
