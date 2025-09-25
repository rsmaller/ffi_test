import ctypes
import platform

if platform.system() == "Darwin":
    extension = ".dylib"
elif platform.system() == "Windows":
    extension = ".dll"
else:
    extension = ".so"

libsort = ctypes.CDLL("libsort" + extension)
libsort.mergeSort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
libsort.outval.argtypes = [ctypes.POINTER(ctypes.c_int)]
libsort.printArgv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char_p)]

def pyMergeSort(myList : list):
    internalCArr = (ctypes.c_int * len(myList))(*myList) # create type on left parenthesis, run type's constructor on unpacked list on right
    length = ctypes.c_int(len(myList))
    libsort.mergeSort(internalCArr, length)
    return list(internalCArr)

def pyOutVal(out):
    libsort.outval(out)

def pyToCArgv(argv):
    argc = len(argv)
    encodedArgv = [item.encode('utf-8') for item in argv]
    return (ctypes.c_char_p * argc)(*encodedArgv)

def printCArgv(argv):
    libsort.printArgv(ctypes.c_int(len(argv)), argv)
