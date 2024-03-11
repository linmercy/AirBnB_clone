#!/usr/bin/python3
"""Command Interpreter Module"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj = storage.all().get(args[1])
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj = storage.all(eval(args[0])).get(args[1])
            if obj is None:
                print("** no instance found **")
            else:
                del storage.all()[args[0] + "." + args[1]]
                storage.save()
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                objs = [str(obj) for obj in storage.all(eval(arg)).values()]
                print(objs)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        try:
            obj_dict = storage.all(eval(args[0]))
            obj = obj_dict.get(args[1])
            if obj is None:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            if hasattr(obj, attr_name):
                attr_value = type(getattr(obj, attr_name))(attr_value)
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** attribute doesn't exist **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

