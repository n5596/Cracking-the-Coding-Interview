class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split(" ")

        if len(slist) != len(pattern):
            return False

        mapping1, mapping2 = {}, {}
        
        n = len(slist)
        for i in range(n):
            if pattern[i] in mapping1 or slist[i] in mapping2:
                if pattern[i] not in mapping1 or slist[i] not in mapping2: # another word/letter is mapped to this one
                    return False
                if mapping1[pattern[i]] != slist[i] or mapping2[slist[i]] != pattern[i]:
                    return False
            else:
                mapping1[pattern[i]] = slist[i]
                mapping2[slist[i]] = pattern[i]
                
        return True
