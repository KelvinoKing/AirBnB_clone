#!/usr/bin/python3
"""module json to serialize and deserialize instances of JSON file
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage():
    """The class serializes and deserializes instances
    of JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """

        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[key] = v.to_dict()

        json_string = json.dumps(new_dict)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_string)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                data = json.load(f)
                for new_dict in data.values():
                    my_class = new_dict['__class__']
                    self.new(eval("{}({})".format(my_class, '**new_dict')))
        except FileNotFoundError:
            pass
