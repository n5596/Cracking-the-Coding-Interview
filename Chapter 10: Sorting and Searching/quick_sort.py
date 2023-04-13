### Quick sort
import random

def partition(array, low, high):
	pivot = array[high-1]
	i = low

	for j in range(low, high):
		if array[j] < pivot: #moving all elements lesser than pivot before it.
			temp = array[i]
			array[i] = array[j]
			array[j] = temp
			i += 1
	temp = array[i] #move pivot in its correct position
	array[i] = pivot
	array[high-1] = temp

	return array, i

def qs_algo(array, low, high): 
	if low >= high:
		return array

	array, pivot_idx = partition(array, low, high)

	array = qs_algo(array, low, pivot_idx)
	array = qs_algo(array, pivot_idx+1, high)
	return array

def quick_sort(array): #O(nlogn) average time, O(n^2) worst time, O(n) space
	n = len(array)
	array = qs_algo(array, 0, n)
	return array

n = random.randint(10,100)
array = []
for i in range(n):
	value = random.randint(1,1000)
	array.append(value)

print('Original array:', array)
qq_array = quick_sort(array)
print('Quick sorted array:', qq_array)
