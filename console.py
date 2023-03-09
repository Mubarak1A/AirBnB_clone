#!/usr/bin/python3
""" Module  contains the entry point of the command interpreter """
import cmd
import models
from models.base_model import BaseModel


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
            print("** class name missing **")
        if arg not in HBNBCommand.class_dic.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.class_dic[arg]()
            HBNBCommand.class_dic[arg].save(obj)
            print(obj.id)

    def do_show(self, arg):
        """ Prints the string representation of an instance
            based on the class name and id

            arg - (string) instance class name and id
        """
        args = arg.split()
        objs = models.storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif arg not in objs:
            print("** no instance found **")
        else:
            print(objs[args[0]+"."+args[1]])

        def do_destroy(self, arg):
            """ Deletes an instance based on the class name and id
                save the change into the JSON file

                arg - (string) instance class name and id
            """
            args = arg.split()
            if not arg:
                print("** class name missing **")
            elif args[0] not in HBNBCommand.class_dict.keys():
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif arg not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[arg]
                models.storage.save()
                
        def do_all(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
