#!/usr/bin/python3
""" Module  contains the entry point of the command interpreter """
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ class that handles command """

    prompt = '(hbnb)'
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

        def do_all(self, arg):
            """ Prints all string representation of all instances
                based or not on the class name

                arg - (string) instance class name
            """
            objs = models.storage.all()
            objs_list = []
            for key, value in objs.items():
                objs_list.append(str(objs.value))
            if arg:
                if arg not in HBNBCommand.class_dic.keys():
                    print("** class doesn't exist **")
                else:
                    if len(obj_list) > 0:
                        print(obj_list)
            else:
                if len(obj_list) > 0:
                    print(obj_list)

            def do_update(self, arg):
                """ Updates an instance based on the class name and id
                    by adding or updating attribute
                    (save the change into the JSON file)

                    arg - (string) class, id, attr name and attr value
                """
                args = arg.split()
                objs = models.storage.all()
                if not arg:
                    print("** class name missing **")
                elif args not in HBNBCommand.class_dic.keys():
                    print("** class doesn't exist **")
                elif len(args) == 1:
                    print("** instance id missing **")
                elif args[0]+"."+args[1] not in objs.keys():
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    obj = objs[args[0]+'.'+args[1]]
                    if args[2] in obj.__dict__.keys():
                        try:
                            if args[3].isdigit():
                                args[3] = int(args[3])
                            elif args[3].replace('.', '', 1).isdigit():
                                args[3] = float(args[3])
                        except AttributeError:
                            pass
                        setattr(obj, args[2], args[3])
                    else:
                        try:
                            if args[3].isdigit():
                                args[3] = int(args[3])
                            elif args[3].replace('.', '', 1).isdigit():
                                args[3] = float(args[3])
                        except AttributeError:
                            pass
                        setattr(obj, args[2], args[3])
                    HBNBCommand.className[args[0]].save(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
