#!/usr/bin/python3
'''HBNBCommand class'''
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        '''Exit'''
        return True

    def do_quit(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
