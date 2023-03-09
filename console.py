#!/usr/bin/python3
""" Module  contains the entry point of the command interpreter """
import cmd
import models
from model.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ class that handles command """

    prompt = '(hbnb) '
    class_dic = {"BaseModel": models.BaseModel,
                 "User": models.User,
                 "State": models.State,
                 "City": models.City,
                 "Amenity": models.Amenity,
                 "Place": models.Place,
                 "Review": models.Review
                 }

    def do_quit(self, arg):
        """ class method to quit program """
        return True

    def do_EOF(self, arg):
        """ class method to quit program """
        print('')
        return True

    def emptyline(self):
        """ shouldn’t execute anything """
        pass

    def help_quit(self):
        """ print help instruction on quit command """
        print("class method to quit program/n")

    def do_create(self, arg):
        """ Creates a new instance (arg) of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        if not arg:
            print(" ** class name missing **")
        if arg not in HBNBCommand.class_dic.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.class_dic[arg]()
            HBNBCommand.class_dic[arg].save(obj)
            print(obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
