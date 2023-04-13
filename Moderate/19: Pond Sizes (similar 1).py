from os import *
from sys import *
from collections import *
from math import *

import sys 
sys.setrecursionlimit(10**7)

def maxAreaOfIsland(grid, n, m):
	# Write your code here.
	
	def find_neighbors(i, j, n, m):
		neighbors = []
		for step1 in [-1, 0, 1]:
			if 0 <= i+step1 and i+step1 < n:
				for step2 in [-1, 0, 1]:
					if 0 <= j+step2 and j+step2 < m:
						neighbors.append((i+step1, j+step2))
		return neighbors

	def dfs(i, j, n, m):
		grid[i][j] = -1

		neighbors = find_neighbors(i, j, n, m)
		count = 1 # current cell

		for next_node in neighbors:
			if grid[next_node[0]][next_node[1]] == 1:
				count += dfs(next_node[0], next_node[1], n, m)
		return count

	max_size = 0
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 1:
				max_size = max(max_size, dfs(i, j, n, m))
	return max_size

# Taking input.
def takeInput() :
	n, m = map(int, sys.stdin.readline().strip().split(" "))
	grid = [list(map(int, sys.stdin.readline().strip().split(" "))) for row in range(n)]
	return n, m, grid

# Main.
t = int(input().strip())
for i in range(t):
	n, m, grid = takeInput()
	ans = maxAreaOfIsland(grid, n, m)
	print(ans)
