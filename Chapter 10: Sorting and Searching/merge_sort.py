### Merge sort
import random

def ms_algo(array, low, high):
	if low+1 == high: #one element
		return [array[low]]

	mid = low + int((high-low)/2)
	
	m1 = ms_algo(array, low, mid)
	m2 = ms_algo(array, mid, high)


	merged = []
	j = 0
	k = 0
	while j < len(m1) and k < len(m2):
		if m1[j] < m2[k]:
			merged.append(m1[j])
			j += 1
		else:
			merged.append(m2[k])
			k += 1

	while j < len(m1):
		merged.append(m1[j])
		j += 1
	while k < len(m2):
		merged.append(m2[k])
		k += 1

	return merged

def merge_sort(array): #O(nlogn) time, O(n) space
	n = len(array)
	array = ms_algo(array, 0, n)
	return array

n = random.randint(10,100)
array = []
for i in range(n):
	value = random.randint(1,1000)
	array.append(value)

print('Original array:', array)
mm_array = merge_sort(array)
print('Merge sorted array:', mm_array)
