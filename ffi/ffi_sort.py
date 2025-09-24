import ctypes
import platform

if (platform.system() == "Darwin"):
    extension = ".dylib"
elif (platform.system() == "Darwin"):
    extension = ".dll"
else:
    extension = ".so"

libsort = ctypes.CDLL("../bin/libsort" + extension)
libsort.mergeSort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]

def pyMergeSort(myList):
    internalCArr = (ctypes.c_int * len(myList))(*myList) # create type on left parenthesis, run type's constructor on unpacked list on right
    length = ctypes.c_int(len(myList))
    libsort.mergeSort(internalCArr, length)
    return list(internalCArr)