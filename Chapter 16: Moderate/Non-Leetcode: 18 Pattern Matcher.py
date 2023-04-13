def check_pattern(s1, s2, sa, sb):
    i = 0
    for j in range(len(s2)):
        if s2[j] == "a" and s1[i:i+len(sa)] == sa:
            i += len(sa)
        elif s2[j] == "b" and s1[i:i+len(sb)] == sb:
            i += len(sb)
        else:
            return False
    return True
        
def pattern_matcher(s1, s2): # s2 consists of only a and b
    n1, n2 = len(s1), len(s2)
    count_a, count_b = 0, 0
    
    for i in range(n2):
        if s2[i] == "a":
            count_a += 1
        else:
            count_b += 1
            
    if s2[0] == "a":
        first_idx_alt = s2.index("b")
    else:
        first_idx_alt = s2.index("a")
        
    for i in range(n1):
        sa = s1[:i+1]
        sa_len = i+1
        rem = n1-sa_len*count_a
        
        if rem > 0 and rem % count_b == 0:
            sb_len = rem // count_b
            
            j = first_idx_alt*sa_len
            sb = s1[j:j+sb_len]
            
            if check_pattern(s1, s2, sa, sb):
                return True
    return False

testcases = [("catcatgocatgo", "aabab", True), ("cbcbd", "ababa", False), ("eefffeeeefff", "abaab", True)]

for t in testcases:
    if pattern_matcher(t[0], t[1]) != t[2]:
        print('Error')
