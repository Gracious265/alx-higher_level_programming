#!/usr/bin/python3
'''
    function to handle open and read files
'''


def read_file(filename=""):
    '''
    function to read a file
    '''

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
