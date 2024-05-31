#!/usr/bin/python3
"""
console module
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB Class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Define quit """
        return True
    
    def do_EOF(self, arg):
        """ Define end of function """
        print ("")
        return True
