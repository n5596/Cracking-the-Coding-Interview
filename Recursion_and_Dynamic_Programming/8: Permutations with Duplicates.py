class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    
        count = {}
        for c in nums:
            count[c] = count.get(c, 0)+1
                    
        all_perms = []
        
        def recurse(seen, rem):
            if rem == 0:
                all_perms.append(seen.copy())
                return
            
            for key in count.keys():
                if count[key] == 0:
                    continue
                    
                count[key] -= 1
                seen.append(key)
                recurse(seen, rem-1)
                seen.pop()
                count[key] += 1
                
            return 
        
        recurse([], len(nums))
        return all_perms
