#!/usr/bin/python3
"""Imported the models.base_model.BaseModel to carry tests on it.
The rest of the imported modules are used by the BaseModel class
"""
import unittest
import json
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel inherits from the TestCase class.
    All test cases of BaseModel class are carried out in this class
    """

    def test_inequality_of_two_different_objects_ids(self):
        """Tests if two obj ids of different instances of BaseModel class
        are equal
        """

        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_inequality_of_two_instances_of_base_model(self):
        """Test if two instances of BaseModel class are equal
        """

        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1, obj2)

    def test_id_is_string(self):
        """Tests if the obj id is a string as it should be
        """

        obj = BaseModel()
        self.assertTrue(isinstance(obj.id, str))

    def test_created_at_attr_is_datetime(self):
        """Test if obj created_at attr is a datetime object
        """

        obj = BaseModel()
        self.assertTrue(isinstance(obj.created_at, datetime))

    def test_updated_at_attr_is_datetime(self):
        """Test if obj updated_at attr is a datetime object
        """

        obj = BaseModel()
        self.assertTrue(isinstance(obj.updated_at, datetime))

    def test_base_model_originates_from_object_class(self):
        """Tests if BaseModel class inherits from the python object class
        """

        obj = BaseModel()
        self.assertIsInstance(obj, object)

    def test_printing_instance_of_base_model(self):
        """Tests if the BaseModel class str() method returns a string in
        a specified format
        """

        obj = BaseModel()
        expected_string = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_string)

    def test_inequality_of_created_at_and_updated_at_after_save(self):
        """Compares the created_at attribute of instnce when object is
        created and after saving. Also compares updated_at attr of instance
        when obj is created and after saving
        """

        obj = BaseModel()
        created_at = obj.created_at
        updated_at = obj.updated_at

        obj.save()

        self.assertEqual(created_at, obj.created_at)
        self.assertNotEqual(updated_at, obj.updated_at)
        self.assertNotEqual(updated_at, created_at)

    def test_inequality_of_more_than_2_different_objects_ids(self):
        """Compares instance ids of more than two instances
        """

        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        obj4 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertNotEqual(obj1.id, obj3.id)
        self.assertNotEqual(obj1.id, obj4.id)
        self.assertNotEqual(obj2.id, obj3.id)
        self.assertNotEqual(obj2.id, obj4.id)
        self.assertNotEqual(obj3.id, obj4.id)

    def test_created_time_less_than_current_time(self):
        """Tests whether the instance created time is less than
        the current time
        """

        obj = BaseModel()
        self.assertTrue(obj.created_at < datetime.now())

    def test_id_is_uuid4_string(self):
        """Tests if an instance id is a uuid4 string
        """

        obj = BaseModel()
        self.assertTrue(len(obj.id) == 36)

    def test_created_at_and_updated_at_format_in_to_dict(self):
        """Tests for the isoformat() used to store the created_at and
        updated_at instance attributes in the dictionary in to_dict() method
        """

        obj = BaseModel()
        obj_dict = obj.to_dict()
        created_at = datetime.strptime(
                obj_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(
                obj_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

    def test_to_dict_method_returns_correct_dictionary(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_deserialization_and_reloading_from_json(self):
        """Checks if an instance2 created using a dictionary attr of
        instance1 is equal to instance1
        """

        obj = BaseModel()
        obj_json = json.dumps(obj.to_dict())
        new_obj = BaseModel(**json.loads(obj_json))
        self.assertEqual(obj.to_dict(), new_obj.to_dict())
        self.assertNotEqual(obj, new_obj)
        self.assertEqual(obj.id, new_obj.id)

    def test_deserialization_and_reloading_from_json2(self):
        """Checks if an instance created with an empyt dict is equal
        to another instance
        """

        obj1 = BaseModel()
        data = {}
        obj2 = BaseModel(**data)

        self.assertNotEqual(obj1.id, obj2.id)


if __name__ == '__main__':
    unittest.main()
