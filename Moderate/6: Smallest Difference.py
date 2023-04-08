from os import *
from sys import *
from collections import *
from math import *

def smallestDifferencePair(arr1, n, arr2, m):

    # Write your code here
    min_diff = 1000000000

    arr1.sort()
    arr2.sort()

    i, j = 0, 0

    while i < n and j < m:
        min_diff = min(min_diff, abs(arr1[i]-arr2[j]))

        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return min_diff
