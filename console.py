#!/usr/bin/python3
"""Module: console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """A HBNBCommand class that inherits from cmd"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quits the console with the quit command"""
        return True

    def do_EOF(self, arg):
        """Quits the console with the EOF command"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
