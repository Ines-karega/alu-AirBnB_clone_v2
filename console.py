#!/usr/bin/python3
"""This module defines the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


CLASSES = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone project."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Exit the program on EOF (Ctrl+D)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER."""
        pass

    def do_create(self, line):
        """Create a new instance of a class, save it, and print its id.

        Usage: create <class name> <param 1> <param 2> ...
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return

        kwargs = {}
        for param in args[1:]:
            if '=' not in param:
                continue
            key, value = param.split('=', 1)

            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1].replace('\\"', '"').replace('_', ' ')
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue

            kwargs[key] = value

        obj = CLASSES[args[0]](**kwargs)
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """Print the string representation of an instance.

        Usage: show <class name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, line):
        """Delete an instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        storage.delete(objects[key])
        storage.save()

    def do_all(self, line):
        """Print all string representations of all instances.

        Usage: all [class name]
        """
        objects = storage.all()
        if line:
            if line not in CLASSES:
                print("** class doesn't exist **")
                return
            result = [
                str(obj) for key, obj in objects.items()
                if key.startswith(line + ".")
            ]
        else:
            result = [str(obj) for obj in objects.values()]
        print(result)

    def do_update(self, line):
        """Update an instance by adding or updating an attribute.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objects[key]
        attr_name = args[2]
        attr_value = args[3]
        if attr_value.startswith('"'):
            attr_value = line.split('"')[1]
        else:
            try:
                if "." in attr_value:
                    attr_value = float(attr_value)
                else:
                    attr_value = int(attr_value)
            except ValueError:
                pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
