### Bubble sort
import random

def bubble_sort(array): #O(n^2) time, O(1) space
	n = len(array)
	for i in range(n):
		for j in range(i+1,n):
			if array[i] > array[j]:
				temp = array[i] 
				array[i] = array[j]
				array[j] = temp
	return array

n = random.randint(10,100)
array = []
for i in range(n):
	value = random.randint(1,1000)
	array.append(value)

print('Original array:', array)
bb_array = bubble_sort(array)
print('Bubble sorted array:', bb_array)

