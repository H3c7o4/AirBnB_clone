#!/usr/bin/env python3
"""This is the console module"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """The console class of our HBNB project."""
    intro = 'Welcome to the HBNB project shell.'
    prompt = '(hbnb)'

    classes = [
            'BaseModel',
            'User',
            'Place',
            'State',
            'City',
            'Amenity',
            'Review'
            ]

    def do_EOF(self, line):
        """
        Exits the programs.
            usage: EOF (Ctrl+D)
        """
        return True

    def do_quit(self, line):
        """
        Exits the program
            usage: quit
        """
        return True

    def emptyline(self):
        """Handles the emptyline behaviour."""
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        if not line:
            print("** class name is missing **")
            return None
        else:
            line = eval(line + '()')
            line.save()
            print(line.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        n = line.split()
        if not line:
            print('** class name missing **')
            return None
        elif (n[0] not in self.classes):
            print("** class doesn't exist **")
            return None
        elif len(n) < 2:
            print('** instance id missing **')
            return None
        else:
            key = '{}.{}'.format(n[0], n[1])
            if key not in storage.all().keys():
                print('** no instance found **')
            else:
                obj = storage.all()
                print(obj[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        n = line.split()
        if not line:
            print('** class name missing **')
            return None
        elif n[0] not in self.classes:
            print('** class doesn\'t exist **')
            return None
        elif len(n) < 2:
            print('** instance id missing **')
            return None
        else:
            key = '{}.{}'.format(n[0], n[1])
            if key not in storage.all().keys():
                print('** no instance found **')
            else:
                obj = storage.all()
                del obj[key]
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        n = line.split()
        obj_list = []
        if len(n) == 0:
            for value in storage.all().values():
                obj_list.append(value.__str__())
            print(obj_list)
        elif (n[0] not in self.classes):
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if n[0] in key:
                    obj_list.append(storage.all()[key].__str__())
                else:
                    return
            print(obj_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
           Usage: update <class name> <id> <attribute name> "<attribute value>"
           Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        n = line.split()
        if not line:
            print('** class name missing **')
            return None
        elif (n[0] not in self.classes):
            print("** class doesn't exist **")
            return None
        elif len(n) < 2:
            print('** instance id missing **')
            return None
        else:
            obj = storage.all()
            key = '{}.{}'.format(n[0], n[1])
            if key not in obj:
                print('** no instance found **')
                return None
            elif len(n) == 2:
                print('** attribute name missing **')
                return None
            elif len(n) == 3:
                print('** value missing **')
                return None
            else:
                setattr(obj[key], n[2], n[3])
                storage.save()
                return None

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        count = 0
        for key in storage.all().keys():
            if line in key:
                count += 1
        print(count)

    def default(self, line):
        """Retrieves instances based on methods.
        Usage : <class name>.all()
        """
        n = line.split('.')
        instance = n[0]
        if n[1] == 'all()':
            self.do_all(instance)
            return None
        elif n[1] == 'count()':
            self.do_count(instance)
            return None
        elif n[1].startswith('show'):
            id_split = n[1].split('"')
            line = instance + ' ' + id_split[1]
            self.do_show(line)
            return None
        elif n[1].startswith('destroy'):
            id_split = n[1].split('"')
            line = instance + ' ' + id_split[1]
            self.do_destroy(line)
            return None
        elif n[1].startswith('update'):
            Args = n[1].split('"')
            line = instance + ' ' + Args[1] + ' ' + Args[3] + ' ' + Args[5]
            self.do_update(line)
            return None


if __name__ == '__main__':
    HBNBCommand().cmdloop()
