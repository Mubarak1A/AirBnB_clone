#!/usr/bin/python3
""" Module  contains the entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """ class that handles command """

    prompt = '(hbnb)'

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
