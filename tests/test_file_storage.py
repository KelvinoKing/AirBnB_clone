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

    def test_create_model_instance(self):
        """Test the 'create_model_instance' method"""

        data = {
            'id': '123',
            'name': 'John Doe',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00'
        }
        instance = self.storage.create_model_instance('User.123', data)
        self.assertIsInstance(instance, User)
        self.assertEqual(instance.id, '123')
        self.assertEqual(instance.name, 'John Doe')


if __name__ == '__main__':
    unittest.main()
