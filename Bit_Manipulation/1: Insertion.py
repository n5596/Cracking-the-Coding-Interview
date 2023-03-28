from os import *
from sys import *
from collections import *
from math import *

def bitInsertion(x, y, a, b):
    # write your code here
    # return an integer denoting the result of inserting Y in X starting from A and ending at B
    
    # clear the bits in x from a to b
    mask1 = 1<<(b+1)
    mask2 = mask1-1

    mask3 = 1<<a
    mask4 = mask3-1

    mask5 = ~mask2|mask4
    x &= mask5

    # add y into x
    shifted_y = y << a
    output = x|shifted_y
    return output
