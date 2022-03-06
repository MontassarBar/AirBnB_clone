#!/usr/bin/python3
'''HBNBCommand class'''
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        '''Quit command to exit the program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        '''an empty line + ENTER shouldn't execute anything'''
        pass

    def do_create(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        line_args = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line_args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(line_args) == 1:
            print("** instance id missing **")
        else:
            id = models.storage.all()
            if (line_args[0] + '.' + line_args[1]) not in id.keys():
                print("** no instance found **")
            else:
                print(id[line_args[0] + '.' + line_args[1]])

    def do_destroy(self, line):
        line_args = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line_args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(line_args) == 1:
            print("** instance id missing **")
        else:
            id = models.storage.all()
            if (line_args[0] + '.' + line_args[1]) not in id.keys():
                print("** no instance found **")
            else:
                del(line_args[0] + '.' + line_args[1])
                models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
