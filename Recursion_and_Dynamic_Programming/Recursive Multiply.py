from os import *
from sys import *
from collections import *
from math import *

def recursiveProduct(m, n):
    # Write your code here
    
    def recursive_multiply(a, b): # a > b
        mod = pow(10,9)+7
        if b == 0:
            return 0
        elif b == 1:
            return a

        flag = False
        if b % 2 == 1:
            flag = True
        b = b >> 1

        half_step = recursive_multiply(a, b)

        curr_step = half_step+half_step
        if flag:
            return int((curr_step+a)%mod)
        return int(curr_step%mod)

    return recursive_multiply(max(m, n), min(m, n))
