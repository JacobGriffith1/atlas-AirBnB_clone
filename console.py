#!/usr/bin/python3
"""
console module
"""

import cmd
import shlex
from models.base_model import BaseModel

class_registry = {
    'BaseModel' : BaseModel,
#add other model classes here, user, place etc

}

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


    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """ Creates new instance of BaseModel and saves it to JSON file """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in class_registry:
            print("** class doesn't exist **")
            return

        # Creates an instance of a class
        new_instance = class_registry[class_name]()
        new_instance.save()
        print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()