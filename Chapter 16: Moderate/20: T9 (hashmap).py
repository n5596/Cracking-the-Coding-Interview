import collections

def find_number(c):
    if c in "abc":
        return 2
    elif c in "def":
        return 3
    elif c in "ghi":
        return 4
    elif c in "jkl":
        return 5
    elif c in "mno":
        return 6
    elif c in "pqrs": 
        return 7
    elif c in "tuv":
        return 8
    elif c in "wxyz":
        return 9 

def convert_to_T9(word):

    code = ""
    for c in word:
        code += str(find_number(c))
    return code

def phoneCode(Words, Sequence, W):
	# Write Your Code Here.
    
    hashmap = {}

    for word in Words:
        code = convert_to_T9(word)

        clist = hashmap.get(code, [])
        clist.append(word)
        hashmap[code] = clist

    return hashmap.get(Sequence, [])
