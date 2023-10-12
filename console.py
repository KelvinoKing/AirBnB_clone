#!/usr/bin/python3
"""cmd modules to build a console
"""
import cmd
import sys
from models.base_model import BaseModel


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
