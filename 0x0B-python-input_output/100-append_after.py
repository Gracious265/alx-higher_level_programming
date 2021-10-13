#!/usr/bin/python3
"""append after"""


def append_after(filename="", search_string="", new_string=""):
    '''append after'''
    with open(filename, mode="r", encoding="utf-8") as myFile:
        new = myFile.readlines()

    with open(filename, mode="w", encoding="utf-8") as io:
        for i in new:
            if search_string in i:
                i = i + new_string
            io.write(i)
