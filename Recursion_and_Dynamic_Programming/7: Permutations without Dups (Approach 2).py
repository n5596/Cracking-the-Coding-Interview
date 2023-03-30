class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        memo = {}
        def recurse(nums):
            if len(nums) == 1:
                return [nums]
            
            curr_perms = []
            n = len(nums)
            for i in range(n):
                new_nums = copy.copy(nums)
                val = new_nums.pop(i)
                prev_perms = recurse(new_nums)
                for perm in prev_perms:
                    perm.insert(0, val)
                curr_perms.extend(prev_perms)
            return curr_perms
        
        return recurse(nums)
