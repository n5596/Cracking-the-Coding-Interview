class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}
        
        for s in strs:
            p = list(s)
            p.sort()
            p = "".join(p)
            
            slist = anagrams.get(p, [])
            slist.append(s)
            anagrams[p] = slist
            
        grouping = []
        for key in anagrams.keys():
            grouping.append(anagrams[key])
            
        return grouping
