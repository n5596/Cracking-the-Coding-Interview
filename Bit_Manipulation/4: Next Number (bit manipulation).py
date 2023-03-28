from os import *
from sys import *
from collections import *
from math import *

def findNextSmallest(n): # p...c1...c0
    temp = n
    c0, c1 = 0, 0
    while temp > 0 and temp % 2 == 0:
        c0 += 1
        temp = temp >> 1

    while temp > 0 and temp % 2 == 1:
        c1 += 1
        temp = temp >> 1

    p = c0+c1

    # clear all bits after p
    mask = 1 << p # (if p == 3, 001000)
    mask = mask-1 # (000111)
    mask = ~mask # (111000)
    n &= mask

    # set p bit
    mask = 1 << p
    n |= mask

    # add c1-1 bits to the least significant positions
    mask = 1<<(c1-1)
    mask = mask-1
    n |= mask
    return n

def findPrevLargest(n): # p...c0...c1
    temp = n
    c0, c1 = 0, 0

    while temp > 0 and temp%2 == 1:
        c1 += 1
        temp = temp >> 1
    
    while temp > 0 and temp%2 == 0:
        c0 += 1
        temp = temp >> 1

    p = c0+c1
    
    # set all bits after p
    mask = 1 << p
    mask = mask-1
    n |= mask

    # clear p bit
    mask = 1 << p
    mask = ~mask
    n &= mask

    # clear c0-1 bits in the least significant positions
    mask = 1 << (c0-1)
    mask = mask-1
    mask = ~mask
    n &= mask
    return n

def nearestNumbers(n):

    # Write your code here
    next_smallest = findNextSmallest(n)
    prev_largest = findPrevLargest(n)
    return [next_smallest, prev_largest]
