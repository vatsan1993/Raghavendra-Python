import math
print(math.gcd(5, 10, 15, 20))


# or
# from math import gdc

import os

print(os.name) # name of the os

print(os.listdir("./")) # lists the files and folders in the specified directory

path = os.path.join("./", "package1") # joins two paths into one.

print(os.listdir(path))

# https://www.geeksforgeeks.org/os-walk-python/
for root, folders, files in os.walk("Sample Dir"):
    print(root)
    print(folders)
    print(files)


# important modules
# os, sys, math, random, itertools, functools, csv, sqlite, json, datetime, tkinter.