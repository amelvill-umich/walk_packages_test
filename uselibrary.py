"""
    Test script for using somelibrary
"""

from __future__ import print_function

from somelibrary import *

print("start of uselibrary.py")

testA = a.aClass()

testA.TestFunction()

testB = b.bClass()

testB.TestFunction()

# Even though there's nothing in empty.py, it's still technically a module
testC = empty

print('empty is ', empty)