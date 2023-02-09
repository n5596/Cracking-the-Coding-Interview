###Check if 2 strings can be made equal by one replacement, one insertion or one deletion

def checkReplace(s1, s2):
	n = len(s1)
	count = 0
	for i in range(n):
		if s1[i] != s2[i]:
			if count > 0:
				return False
			count += 1
	return True

def checkInsert(s1, s2):
	n = len(s2)
	j = 0
	k = 0
	
	count = 0
	while j<n-1 and k<n:
		if s1[j] == s2[k]:
			j += 1
			k += 1
		else:
			count += 1
			k += 1
			if count > 1:
				return False
	return True

print('Input 2 string:')
s1 = input()
s2 = input()

n1 = len(s1)
n2 = len(s2)

if n1 == n2:
	print(checkReplace(s1,s2))
elif n1+1 == n2:
	print(checkInsert(s1,s2))
elif n2+1 == n1:
	print(checkInsert(s2,s1))
else:
	print('Not possible')
