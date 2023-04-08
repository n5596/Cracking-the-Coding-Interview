from os import *
from sys import *
from collections import *
from math import *

def swap(a, b):
    # Write your coder here.
    a = a+b
    b = a-b # b = a+b-b = a
    a = a-b # a = a+b-a = b
    return a,b
