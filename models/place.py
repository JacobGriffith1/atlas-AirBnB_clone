#!/usr/bin/python3
"""
console module
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB Class"""
    prompt = '(hbnb) '
    
    def do_quit(self, argument):
        """ Define quit """
        return True
    
    def do_EOF(self, arguemtn):
        """ Define end of function """
        return True
