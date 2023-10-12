#!/usr/bin/python3
"""cmd modules to build a console
"""
import cmd
import sys


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
