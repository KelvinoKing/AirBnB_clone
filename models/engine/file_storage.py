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
    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    @classmethod
    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    @classmethod
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(self.__objects, f)

    @classmethod
    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r') as f:
               self.__objects = json.load(f)
        except:
            pass
