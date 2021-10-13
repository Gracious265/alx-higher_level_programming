#!/usr/bin/python3
"""function that appends a string to the end"""


def append_write(filename="", text=""):
    """docstring for append"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
