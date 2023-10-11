#!/usr/bin/python3

"""uuid module provides
immutable UUIB objects

datetime module provides classes for
manipulating date and time
"""
import uuid
from datetime import datetime


class BaseModel(object):
    """
    The class will define all common attributes for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        BaseModel class inherits from object class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """String representation of the BaseModel
        """

        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute updated_at with
        the current datetime
        """

        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance
        """

        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--------------")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key]))

    print("--------------")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("---------------------")
    print(my_model is my_new_model)
