#!/usr/bin/python3
'''HBNBCommand class'''
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Quit command to exit the program\n")

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
