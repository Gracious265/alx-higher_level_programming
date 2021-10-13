#!/usr/bin/python3
'''
    Implementing a Geometry class
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
        Implementing the class Square
    '''

    def __init__(self, size):
        '''
        initialize the square class
        take the init from rectangle class
        take the method integer validator from baseGeometry
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''
        define the area to the square
        '''
        return (self.__size ** 2)
