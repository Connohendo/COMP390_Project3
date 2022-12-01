import sys
import util_funcs
import os
import json
from lock_functions import lock
from unlock_functions import unlock
import print_functions
import command_functions
"""Main file with main"""


def parse_command_line_args(arg_list: list):
    """This function helps us process the command sent by the user"""
    arg_list_len = len(arg_list)
    if arg_list_len == 1:
        print('\n\tWelcome to JLOCK!\n'
              '\tby J. Matta\n'
              '\t(c) November 2022\n'
              '\n\tType \'jlock.py -h\' or \'jlock.py -help\' for a list of available commands.\n')
    elif arg_list_len == 2:
        command = arg_list[1]
        if command == '-help' or command == '-h':
            command_functions.help_command()
        elif command == '-msg':
            command_functions.msg_command()
        elif command == '-locked':
            command_functions.locked_command()
        elif command == '-clear':
            command_functions.clear_command()
        else:
            print('Error: invalid command')
    elif arg_list_len == 3:
        if arg_list[1] == '-unlock':
            command_functions.unlock_command(arg_list)
        else:
            print('Error: invalid command')
    elif arg_list_len == 4:
        if arg_list[1] == '-lock':
            command_functions.lock(arg_list)
        else:
            print('Error: invalid command')
    else:
        print('Error: invalid command')


def jlock_main():
    # get command line arguments
    arg_list = sys.argv
    # check for empty string in command line args - empty strings are invalid input
    if '' in arg_list:
        print('Error: invalid command')
        return
    # call for the command passed to be processed by above function
    parse_command_line_args(arg_list)


if __name__ == '__main__':
    jlock_main()
