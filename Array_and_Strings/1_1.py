### Determine if a string has only unique characters
import numpy as np

def count_based(string):
	n = len(string)
	count = [0]*26
	for i in range(n):
		value = ord(string[i])-ord('a')
		if count[value] > 0:
			return False
		count[value] += 1
	return True

def bit_based(string):
	n = len(string)
	bit_vector = 0
	for i in range(n):
		value = ord(string[i])-ord('a')
		mask = 1<<value #want to set the value^th bit position
	
		if mask & bit_vector > 0: #already set
			return False
		bit_vector = bit_vector | mask #set it
	return True

def brute_force(string):
	n = len(string)
	
	for i in range(n):
		for j in range(i+1,n):
			if string[i] == string[j]:
				return False
	return True

def sorting(string):
	n = len(string)
	string = sorted(string)
	for i in range(n-1):
		if string[i] == string[i+1]:
			return False
	return True

print('Give an input string:')
input_str = input()
print('Count based: O(n) time and O(n) space =======>', count_based(input_str))
print('Bit based: O(n) time and O(1) space =========>', bit_based(input_str))
print('Brute force: O(n^2) time and O(1) space =====>', brute_force(input_str))
print('Sorting: O(nlogn) time and O(n) space =======>', sorting(input_str))

