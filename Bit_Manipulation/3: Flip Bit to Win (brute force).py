from os import *
from sys import *
from collections import *
from math import *

def flipBit(a):
    # Write your code here.
    
    looking_for = 0
    count = 0
    seq = []

    while a > 0:
        if a % 2 == looking_for:
            count += 1
        else:
            seq.append(count)
            count = 1
            looking_for = 1-looking_for
        a = a >> 1 # divide by 2
    seq.append(count)

    max_count = 0
    for i in range(0, len(seq), 2):
        zeros_seq = seq[i]
        ones_to_left, ones_to_right = 0, 0
        if i-1 >= 0:
            ones_to_left = seq[i-1]
        if i+1 < len(seq):
            ones_to_right = seq[i+1]

        if zeros_seq == 1:
            max_count = max(max_count, 1+ones_to_left+ones_to_right)
        else:
            max_count = max(max_count, ones_to_left+1, ones_to_right+1)

    return max_count
