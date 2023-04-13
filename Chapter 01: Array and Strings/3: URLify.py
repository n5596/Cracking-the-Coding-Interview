from os import *
from sys import *
from collections import *
from math import *

def replaceSpaces(str):
    # Write your code here.
    
    i = len(str)-1
    spaces = 0
    for c in str:
        if c == " ":
            spaces += 1

    # add 2 spaces for each space (space = 3 characters)
    slist = list(str)
    for k in range(spaces):
        slist.append(" ")
        slist.append(" ")

    j = len(slist)-1

    while i >= 0:
        if str[i] != " ":
            slist[j] = slist[i]
            j -= 1
        else:
            slist[j] = "0"
            slist[j-1] = "4"
            slist[j-2] = "@"
            j -= 3
            
        i -= 1
    return "".join(slist)
