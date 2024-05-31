#!/usr/bin/python3
"""
console module
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class_registry = {
    'BaseModel': BaseModel,
    # Add other model classes here, e.g., 'User': User, 'Place': Place, etc.
}

class HBNBCommand(cmd.Cmd):
    """HBNB Class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Define quit"""
        return True
    
    def do_EOF(self, arg):
        """Define end of function"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel and saves it to JSON file"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in class_registry:
            print("** class doesn't exist **")
            return

        # Create an instance of the class
        new_instance = class_registry[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()