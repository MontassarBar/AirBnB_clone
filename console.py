#!/usr/bin/python3
'''HBNBCommand class'''
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        '''Exit'''
        return True

    def do_quit(self, arg):
        '''Exit'''
        sys.exit(1)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
