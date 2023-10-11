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

    @classmethod
    def all(cls):
        """Returns the dictionary __objects
        """
        return  cls.__objects

    @classmethod
    def new(cls, obj):
        """sets in __objects the obj with key
        <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        print(key)
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """serializes __objects to the JSON file (path: __file_path)
        """
        with open(cls.__file_path, 'w', encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in cls.__objects.items()}, f)

    @classmethod
    def reload(cls):
        from models import base_model

        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(cls.__file_path, 'r', encoding="utf-8") as f:
                cls.__objects = {k: base_model.BaseModel(**v) for k, v in json.load(f).items()}
        except FileNotFoundError:
            pass
