#!/usr/bin/python3
"""import city module to build tests
and unittest
"""
from models.city import City
from models.base_model import BaseModel
import unittest
import json
from datetime import datetime


class TestCity(unittest.TestCase):
    """TestCity inherits from the TestCase class.
    All test cases of City class are carried out in this class
    """

    def test_inequality_of_two_different_objects_ids(self):
        """Tests if two obj ids of different instances of City class
        are equal
        """

        obj1 = City()
        obj2 = City()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_inequality_of_two_instances_of_city(self):
        """Test if two instances of City class are equal
        """

        obj1 = City()
        obj2 = City()
        self.assertNotEqual(obj1, obj2)

    def test_id_is_string(self):
        """Tests if the obj id is a string as it should be
        """

        obj = City()
        self.assertTrue(isinstance(obj.id, str))

    def test_name_is_string(self):
        """Tests if attr 'first_name' is a string
        """

        obj = City()
        self.assertTrue(isinstance(obj.name, str))

    def test_state_id_attr_is_string(self):
        """Tests if attr 'state_id' is a string
        """

        obj = City()
        self.assertTrue(isinstance(obj.state_id, str))

    def test_city_originates_from_base_model(self):
        """Tests if City class inherits from the python object class
        """

        obj = City()
        self.assertIsInstance(obj, BaseModel)

    def test_printing_instance_of_city(self):
        """Tests if the City class str() method returns a string in
        a specified format
        """

        obj = City()
        expected_string = f"[City] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_string)

    def test_inequality_of_created_at_and_updated_at_after_save(self):
        """Compares the created_at attribute of instnce when object is
        created and after saving. Also compares updated_at attr of instance
        when obj is created and after saving
        """

        obj = City()
        created_at = obj.created_at
        updated_at = obj.updated_at

        obj.save()

        self.assertEqual(created_at, obj.created_at)
        self.assertNotEqual(updated_at, obj.updated_at)
        self.assertEqual(updated_at, created_at)

    def test_inequality_of_more_than_2_different_objects_ids(self):
        """Compares instance ids of more than two instances
        """

        obj1 = City()
        obj2 = City()
        obj3 = City()
        obj4 = City()
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

        obj = City()
        self.assertTrue(obj.created_at < datetime.now())

    def test_id_is_uuid4_string(self):
        """Tests if an instance id is a uuid4 string
        """

        obj = City()
        self.assertTrue(len(obj.id) == 36)

    def test_created_at_and_updated_at_format_in_to_dict(self):
        """Tests for the isoformat() used to store the created_at and
        updated_at instance attributes in the dictionary in to_dict() method
        """

        obj = City()
        obj_dict = obj.to_dict()
        created_at = datetime.strptime(
                obj_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(
                obj_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

    def test_to_dict_method_returns_correct_dictionary(self):
        obj = City()
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

        obj = City()
        obj_json = json.dumps(obj.to_dict())
        new_obj = City(**json.loads(obj_json))
        self.assertEqual(obj.to_dict(), new_obj.to_dict())
        self.assertNotEqual(obj, new_obj)
        self.assertEqual(obj.id, new_obj.id)

    def test_deserialization_and_reloading_from_json2(self):
        """Checks if an instance created with an empyt dict is equal
        to another instance
        """

        obj1 = City()
        data = {}
        obj2 = City(**data)

        self.assertNotEqual(obj1.id, obj2.id)


if __name__ == '__main__':
    unittest.main()
