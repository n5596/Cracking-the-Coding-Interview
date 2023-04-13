class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        c1, c2 = {}, {}
        
        for c in s:
            c1[c] = c1.get(c, 0)+1
        for c in t:
            c2[c] = c2.get(c, 0)+1
            
        keys1, keys2 = c1.keys(), c2.keys()
        
        # if either set of keys contain a unique element
        if set(keys1)-set(keys2) != set() or set(keys2)-set(keys1) != set():
            return False
        
        for key in keys1:
            if c1[key] != c2[key]:
                return False
        return True
