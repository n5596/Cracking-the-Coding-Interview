class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def recurse(idx, n):
            if idx == n:
                return [[]]
            
            prev_perms = recurse(idx+1, n)
            curr_perms = []
            
            for perm in prev_perms:
                for j in range(len(perm)+1):
                    new_perm = copy.copy(perm)
                    new_perm.insert(j, nums[idx])
                    curr_perms.append(new_perm)
                    
            return curr_perms
        
        return recurse(0, len(nums))
