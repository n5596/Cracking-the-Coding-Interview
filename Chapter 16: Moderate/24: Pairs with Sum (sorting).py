class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        l, r = 0, len(nums)-1
        sum_val = 0
        operations = 0
        
        while l < r:
            sum_val = nums[l] + nums[r]
            
            if sum_val == k:
                operations += 1
                l += 1
                r -= 1
            elif sum_val < k:
                l += 1
            else:
                r -= 1
                
        return operations
