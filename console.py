#!/usr/bin/python3
"""Command interpreter module."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
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
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key in objs:
                print(objs[key])
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key in objs:
                del objs[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            objs = storage.all()
            print([str(objs[key]) for key in objs])
        else:
            try:
                if arg not in storage.classes():
                    print("** class doesn't exist **")
                    return
                objs = storage.all()
                filtered_objs = {key: objs[key] for key in objs if key.split('.')[0] == arg}
                print([str(obj) for obj in filtered_objs.values()])
            except IndexError:
                print("** instance id missing **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in objs:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            setattr(objs[key], args[2], args[3][1:-1])
            storage.save()
        except IndexError:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

