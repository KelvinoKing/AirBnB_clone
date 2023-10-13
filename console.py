#!/usr/bin/python3
"""cmd modules to build a console
"""
import cmd
import sys
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple python console
    """

    prompt = "(hbnb) "

    if sys.stdin.isatty():
        pass
    else:
        def postloop(self):
            """Formats the output when running in non-interactive mode"""
            print()

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file
        and prints the id
        """
        my_args = parse(arg)

        if len(my_args) == 0:
            print("** class name missing **")
        else:
            if my_args[0] == "BaseModel":
                obj = BaseModel()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id"""
        my_args = parse(arg)

        if len(my_args) == 0:
            print("** class name missing **")
        elif len(my_args) == 1:
            print("** instance id missing **")
        elif len(my_args) == 2:
            if my_args[0] == "BaseModel":

                # Convert the dictionary of objects returned by storage.all()
                # to a dictionary of dictionary of objects attributes
                all_objs = storage.all()
                returned_obj_id = search(my_args[1], all_objs)
                if returned_obj_id is not None:
                    print(all_objs[returned_obj_id])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroys an instance based on the class name and id
        """
        my_args = parse(arg)

        if len(my_args) == 0:
            print("** class name missing **")
        elif len(my_args) == 1:
            print("** instance id missing **")
        elif len(my_args) == 2:
            if my_args[0] == "BaseModel":
                all_objs = storage.all()
                del_obj = search(my_args[1], all_objs)

                if del_obj is not None:
                    del all_objs[del_obj]
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string rep of all instaces based or not on
        the class name
        """
        my_args = parse(arg)

        all_objs = storage.all()
        obj_rep_str = []

        if len(my_args) == 1:
            if my_args[0] == "BaseModel":
                for k, v in all_objs.items():
                    obj_str = v.__str__()
                    obj_rep_str.append(obj_str)
                print(obj_rep_str)
            else:
                print("** class doesn't exist **")
        else:
            for k, v in all_objs.items():
                obj_str = v.__str__()
                obj_rep_str.append(obj_str)
            print(obj_rep_str)

    def do_update(self, arg):
        """Updates an instance based on class name and id by adding or
        updating attributes"""

        my_args = parse(arg)
        if len(my_args) == 0:
            print("** class name missing **")
        elif my_args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(my_args) == 1:
            print("** instance id missing **")
        elif len(my_args) >= 2:
            all_obj = storage.all()
            returned_obj_id = search(my_args[1], all_obj)

            if returned_obj_id is not None:
                if len(my_args) == 2:
                    print("** attribute name missing **")
                elif len(my_args) == 3:
                    print("** value missing **")
                elif len(my_args) >= 4:
                    obj = all_obj[returned_obj_id]
                    try:
                        value = eval(my_args[3])
                    except Exception:
                        value = my_args[3]
                    setattr(obj, my_args[2], value)
                    models.storage.save()
            else:
                print("** no instance found **")

    def do_EOF(self, arg):
        """Exit the console when EOF command is passed"""
        return True

    def do_quit(self, arg):
        """Exits the console when quit command is passed\n"""
        return True

    def emptyline(self):
        """Does not execute previous command when empty line +
        ENTER are passed to the prompt\n"""
        pass


def parse(arg):
    """conver arg to a tuple of args and return tuple
    """
    return tuple(map(str, arg.split()))


def search(obj_id, all_objs):
    """searches for object and returns found object or None
    """
    new_objs = {}

    for k, v in all_objs.items():
        new_objs[k] = v.to_dict()

    # First loop takes one dict at a time
    # second loop compares the keys
    for k, v in new_objs.items():
        new_dict = v

        for key, value in new_dict.items():
            if key == 'id':
                if obj_id == v[key]:
                    return k
            else:
                break

    return None


if __name__ == "__main__":
    HBNBCommand().cmdloop()