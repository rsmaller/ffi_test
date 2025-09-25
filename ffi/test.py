#!/usr/bin/python3
import ctypes
import sys
import os
from ffi_sort import *

print("Ran from " + os.getcwd())
print("Script lives in " + os.path.dirname(__file__))

myList = [4, 3, 2, 1]
print(f"My list: {myList}")
myList = pyMergeSort(myList)
print(f"After sort: {myList}")

myInt = ctypes.c_int(0)
print(f"My integer is {myInt}")
pyOutVal(ctypes.byref(myInt))
print(f"After, my integer is {myInt}")

cargv = pyToCArgv(sys.argv)
printCArgv(cargv)