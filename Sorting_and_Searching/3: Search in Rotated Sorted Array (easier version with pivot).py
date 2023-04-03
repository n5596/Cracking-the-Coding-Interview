class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums, l, r, target):
            if l > r:
                return -1
            
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return binary_search(nums, mid+1, r, target)
            else:
                return binary_search(nums, l, mid-1, target)
            
        pivot = -1
        n = len(nums)
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                pivot = i+1
                break
                
        if pivot == -1:
            return binary_search(nums, 0, n-1, target)
        
        left_half = nums[:pivot]
        left_val = binary_search(left_half, 0, len(left_half)-1, target)
        
        if left_val != -1:
            return left_val
        
        right_half = nums[pivot:]
        right_val = binary_search(right_half, 0, len(right_half)-1, target)
        
        if right_val != -1:
            right_val += len(left_half)
        return right_val
