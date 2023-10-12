#!/usr/bin/python3
"""cmd modules to build a console
"""
import cmd
import sys
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
                new_objs = {}
                count = 0
                for k, v in all_objs.items():
                    new_objs[k] = v.to_dict()

                # First loop takes one doctionary at a time
                # Second loop compares the keys
                for k, v in new_objs.items():
                    if count == 1:
                        break
                    new_dict = v
                    for key, value in new_dict.items():
                        if key == 'id':
                            if my_args[1] == v[key]:
                                print(all_objs[k])
                                count += 1
                                break
                            else:
                                break
                if count == 0:
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

                # Convert the dictionary of objects returned by storage.all()
                # to a dictionary of dictionary of objects attributes
                all_objs = storage.all()
                new_objs = {}
                count = 0
                for k, v in all_objs.items():
                    new_objs[k] = v.to_dict()

                # First loop takes one doctionary at a time
                # Second loop compares the keys
                for k, v in new_objs.items():
                    if count == 1:
                        break
                    new_dict = v
                    for key, value in new_dict.items():
                        if key == 'id':
                            if my_args[1] == v[key]:
                                new_key = k
                                count += 1
                                break
                            else:
                                break
                if count == 0:
                    print("** no instance found **")
                if count == 1:
                    del all_objs[new_key]
                    for k, v in all_objs.items():
                        v.save()
            else:
                print("** class doesn't exist **")

    def do_EOF(self, line):
        """Exit the console when EOF command is passed"""
        return True

    def do_quit(self, line):
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
