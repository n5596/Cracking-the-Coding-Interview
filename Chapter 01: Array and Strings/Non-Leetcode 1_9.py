### Check if s1 (erbottlewat) is a rotation of s2 (waterbottle)

def checkSubstring(s1, s2):
	#if s1 in s2:
	#	return True

	for i in range(len(s2)-len(s1)):
		if s1 == s2[i:i+len(s1)]:
			return True
	return False

print('Input 2 strings:')
s1 = input()
s2 = input()

print('Is s1 a rotation of s2:', checkSubstring(s1,s2+s2))

