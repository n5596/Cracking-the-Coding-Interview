from os import *
from sys import *
from collections import *
from math import *

def ninjaAnt(arr, sr, sc, moves):
    # Write your code here.

    r, c = sr, sc
    m, n = len(arr), len(arr[0])

    direction = "RIGHT"

    def rotate_clockwise(curr_direction):
        next_dir = {"TOP":"RIGHT", "RIGHT":"BOTTOM","BOTTOM":"LEFT","LEFT":"TOP"}
        return next_dir[curr_direction]

    def rotate_counterclockwise(curr_direction):
        next_dir = {"TOP":"LEFT","LEFT":"BOTTOM","BOTTOM":"RIGHT","RIGHT":"TOP"}
        return next_dir[curr_direction]

    for i in range(moves):
        if arr[r][c] == 1: # clockwise
            direction = rotate_clockwise(direction)
        else: # counter clockwise
            direction = rotate_counterclockwise(direction)

        arr[r][c] = 1-arr[r][c] # invert
        
        if direction == "RIGHT":
            c += 1
        elif direction == "BOTTOM":
            r += 1
        elif direction == "LEFT":
            c -= 1
        else:
            r -= 1

        if r < 0 or r >= m or c < 0 or c >= n: # exits matrix
            return -1,-1

    return r,c
