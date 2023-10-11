#!/usr/bin/python3

"""uuid module provides
immutable UUIB objects

datetime module provides classes for
manipulating date and time
"""
import uuid
from datetime import datetime
from models import storage


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
        storage.new(self)

        if kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            storage.new(self)

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
        storage.save()

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
    from models import storage
    from models.base_model import BaseModel

    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
