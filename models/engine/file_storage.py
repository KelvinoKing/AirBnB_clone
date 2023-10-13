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
            serialized_data = {
                    k: v.to_dict() for k, v in self.__objects.items()
                    }
            json.dump(serialized_data, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                data = json.load(f)
                self.__objects = {
                        k: self.create_model_instance(
                            k, v) for k, v in data.items()}
        except Exception:
            pass

    def create_model_instance(self, key, data):
        """create an object of the specified class
        """
        from models import base_model

        class_name, obj_id = key.split(".")
        if class_name == "User":
            from models.user import User
            model_class = User
        else:
            model_class = getattr(base_model, class_name)
        obj = model_class(**data)
        return obj
