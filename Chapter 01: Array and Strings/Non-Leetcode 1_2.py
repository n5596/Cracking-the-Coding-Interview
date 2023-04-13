### Determine if 2 strings are permutations of one another

def sorting(s1, s2):
	n1 = len(s1)
	n2 = len(s2)
	if n1 != n2:
		return False

	s1 = sorted(s1)
	s2 = sorted(s2)

	for i in range(n1):
		if s1[i] != s2[i]:
			return False
	return True

def char_counts(s1, s2):
	n1 = len(s1)
	n2 = len(s2)
	if n1 != n2:
		return False

	count1 = [0]*26
	count2 = [0]*26

	for i in range(n1):
		v1 = ord(s1[i])-ord('a')
		v2 = ord(s2[i])-ord('a')
		count1[v1] += 1
		count2[v2] += 1

	for i in range(26):
		if count1[i] != count2[i]:
			return False
	return True

print('Give 2 input strings:')
s1 = input()
s2 = input()
print('Sorting based: O(nlogn) time =====>', sorting(s1,s2))
print('Character count based: O(n) time and O(n) space ===>', char_counts(s1,s2))
