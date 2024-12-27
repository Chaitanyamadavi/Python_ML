# a array in python has a fixed size that's why we use dynamic array which can change it's size according to the needs of the user.

# dynamic array

#ctypes is a foreign library in python, using which you can create the Data types of C in python 

import ctypes
class MeraList:
    def __init__(self):
        self.size =1 
        self.n = 0

# create a C type array with size = self.size
    self.A