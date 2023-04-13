from os import *
from sys import *
from collections import *
from math import *

def sparseSearch(arr, k):
	# Write your code here.
	
	def binary_search(l, r, target):
		if l > r:
			return -1

		mid = (l+r)//2

		if arr[mid] == "": # find the closest non-empty string
			i, j = mid-1, mid+1

			while i >= l and j <= r:
				if arr[i] != "":
					mid = i
					break
				elif arr[j] != "":
					mid = j
					break
				else:
					i -= 1
					j += 1

		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			return binary_search(mid+1, r, target)
		else:
			return binary_search(l, mid-1, target)

	return binary_search(0, len(arr)-1, k)
