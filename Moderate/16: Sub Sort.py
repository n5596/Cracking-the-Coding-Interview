class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        if n <= 1:
            return 0
        
        left_end, right_start = -1, -1
        
        for i in range(n):
            if i == n-1: # array is completely sorted
                return 0
            
            if nums[i] > nums[i+1]: # not in order
                break
                
        left_end = i
        
        for j in range(n-1, 0, -1):
            if nums[j-1] > nums[j]: # not in order
                break
                
        right_start = j
        
        min_yet = min(nums[left_end+1:])
        max_yet = max(nums[:right_start])
        
        while left_end >= 0 and nums[left_end] > min_yet:
            left_end -= 1
            
        while right_start < n and nums[right_start] < max_yet:
            right_start += 1
            
        return (right_start-1)-(left_end+1)+1
