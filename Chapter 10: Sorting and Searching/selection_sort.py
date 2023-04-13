### Selection sort
import random

def selection_sort(array): #O(n^2) time, O(1) space
	n = len(array)
	for i in range(n):
		minimum = 10000000
		pos = -1
		for j in range(i,n):
			if minimum > array[j]:
				minimum = array[j]
				pos = j
		if pos != -1: #swap
			temp = array[i]
			array[i] = minimum
			array[pos] = temp
	return array

n = random.randint(10,100)
array = []
for i in range(n):
	value = random.randint(1,1000)
	array.append(value)

print('Original array:', array)
ss_array = selection_sort(array)
print('Selection sorted array:', ss_array)
