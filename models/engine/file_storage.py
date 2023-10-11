#!/usr/bin/python3
"""module json to serialize and deserialize instances of JSON file
"""
import json


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
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        from models import base_model
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects =
                {k: base_model.BaseModel(**v) for k, v in json.load(f).items()}
        except Exception:
            pass
