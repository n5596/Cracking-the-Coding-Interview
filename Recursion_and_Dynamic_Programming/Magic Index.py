# duplicates allowed
from os import *
from sys import *
from collections import *
from math import *

def magicIndex(a, n):
    # write your code here
    # return an integer denoting the answer
    
    def binary_search(l, r):
        if l > r:
            return -1

        mid = (l+r)//2
        
        if a[mid] == mid:
            return mid
    
        left = binary_search(l, min(mid-1, a[mid]))
        if left != -1: # found
            return left

        right = binary_search(mid+1, r)
        return right
    return binary_search(0, n-1)
