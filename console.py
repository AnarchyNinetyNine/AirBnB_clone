#!/usr/bin/python3
""" HBNBCommand console for HBNB """


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, class_name_arg):

        """Create a new instance of BaseModel, save it, and print the id"""

        if not class_name_arg:
            print("** class name missing **")
            return

        try:
            model_class = globals()[class_name_arg]
            new_instance = model_class()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):

        """Show an instance based on the class name and id"""

        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, obj_id = args[0], args[1]

        try:
            model_class = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"

        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):

        """ Deletes an instance based on the class name and id """

        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, obj_id = args[0], args[1]

        try:
            model_class = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"

        if key in storage.all():
            del storage.all()[key]
        else:
            print("** no instance found **")

    def do_all(self, class_name):

        """
        Prints all string representations of all instances of a given class.
        If no class name is given, print all instances of all classes

        Args:
            class_name (str): The name of the class to print instances of.
        """

        objects = storage.all()

        if not class_name:

            """
            If no class name is given,
            print all instances of all classes
            """
            arr = [str(obj) for obj in objects.values()]
            print(arr)
            return

        try:
            """ Try to get the class from globals """
            model_class = globals()[class_name]
        except KeyError:
            """ If the class does not exist, print an error message """
            print("** class doesn't exist **")
            return

        arr = []
        for key, obj in objects.items():
            """ Check if the object's class matches the given class name """
            if key.split('.')[0] == class_name:
                arr.append(str(obj))
        print(arr)

    def do_update(self, line):

        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"

        Args:
            line (str): Command line input in the format of
                '<class name> <id> <attribute name> "<attribute value>"'.

        Error Management:
            - If the class name is missing, print ** class name missing **
            - If the class name doesn’t exist, print ** class doesn't exist **
            - If the id is missing, print ** instance id missing **
            - If the instance of the class name doesn’t exist for the id,
              print ** no instance found **
            - If the attribute name is missing,
              print ** attribute name missing **
            - If the value for the attribute name doesn’t exist,
              print ** value missing **
        """

        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attr_value = args[3]
        obj = storage.all()[key]

        """ Convert value to the appropriate type """
        attr_type = type(getattr(obj, attr_name, str))

        try:
            attr_value = attr_type(attr_value.strip('"'))
        except ValueError:
            print("** invalid value **")
            return

        setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, line):
        """Override the default method to handle <class name>.*()"""

        args = line.split('.')
        instances = 0

        if not args[0] in globals() or len(args) != 2:
            print(f"*** Unknown syntax: {line}")

        if args[1] == "all()":
            self.do_all(args[0])
        elif args[1] == "count()":
            for key, value in storage.all().items():
                if key.split('.')[0] == args[0]:
                    instances += 1
            print(instances)
        elif args[1].startswith("show(") and args[1].endswith(")"):
            instance_id = args[1][5:-1].strip('"')
            self.do_show(f"{args[0]} {instance_id}")
        elif args[1].startswith("destroy(") and args[1].endswith(")"):
            instance_id = args[1][8: -1].strip('"')
            self.do_destroy(f"{args[0]} {instance_id}")
        else:
            print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
