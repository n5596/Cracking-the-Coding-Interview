from os import *
from sys import *
from collections import *
from math import *

def swap(a, b):
    # Write your coder here.
    a = a ^ b 
    # a = 0 if original_a and original_b are same
    # a = 1 if original_a and original_b are different
    
    b = a ^ b 
    # {0 if same, 1 if different} ^ b
    # = bits where original_a and original_b are same will remain unchanged
    # and bits where original_a and original_b differ will be flipped
    # = only change is at the bits where original_a and original_b differ and these bits will be flipped
    # = since only difference between original_a and original_b is at these bits, flipping them will convert 
    # original_b to original_a = a

    a = a ^ b
    # {0 if same, 1 if different} ^ a
    # = only change is at the bits where original_a and original_b differ and these bits are flipped
    # = flipping these bits will convert a^b to original_b = b
    return a,b
