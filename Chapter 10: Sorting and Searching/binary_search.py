### Binary search
import random

def binary_search(array, low, high, value): #O(nlogn) time, O(1) space
	if high <= low:
		return 0

	mid = low+int((high-low)/2)
	
	if array[mid] == value:
		print('Found value at position ', mid)
		return 1

	if value < array[mid]:
		ans = binary_search(array, low, mid, value)
	else:
		ans = binary_search(array, mid+1, high, value)

	if low == 0 and high == len(array) and ans == 0:
		print('Could not find value.')
	return ans

n = random.randint(10,100)
array = []
for i in range(n):
	value = random.randint(1,100)
	array.append(value)

value = random.randint(1,100)
array.sort()
print('Finding ', value, ' in sorted array: ', array)
ans = binary_search(array, 0, len(array), value)
