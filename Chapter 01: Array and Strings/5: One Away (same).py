class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        # write your code here

        def oneEditAway(u, v): # len(v) = len(u)+1
            n = len(v)

            i, j = 0, 0
            count = 0
            while i < n-1 and j < n:
                if u[i] != v[j]:
                    if count > 0:
                        return False
                    count += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            return True

        n1, n2 = len(s), len(t)
        if abs(n1-n2) > 1:
            return False
        
        if n1 == n2:
            if s == t:
                return False
            count = 0
            for i in range(n1):
                if s[i] != t[i]:
                    if count > 0:
                        return False
                    count += 1
            return True
        else:
            if n1 > n2:
                return oneEditAway(t, s)
            else:
                return oneEditAway(s, t)
