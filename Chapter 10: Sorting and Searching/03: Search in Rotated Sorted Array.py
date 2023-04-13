class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def binary_search(l, r, target):
            if l > r:
                return False
            
            mid = (l+r)//2
            
            if nums[mid] == target:
                return True
            elif nums[l] < nums[mid]: # first half is sorted
                
                if nums[l] <= target and target < nums[mid]:
                    return binary_search(l, mid-1, target)
                return binary_search(mid+1, r, target)
            
            elif nums[mid] < nums[r]: # second half is sorted
                
                if nums[mid] < target and target <= nums[r]:
                    return binary_search(mid+1, r, target)
                return binary_search(l, mid-1, target)
            
            elif nums[l] == nums[mid]:
                
                if nums[mid] != nums[r]:
                    return binary_search(mid+1, r, target)
                else: # search both halves
                    left_half = binary_search(l, mid-1, target)
                    if left_half:
                        return True
                    return binary_search(mid+1, r, target)
            
            elif nums[mid] == nums[r]:
                
                if nums[mid] != nums[l]:
                    return binary_search(l, mid-1, target)
                else:
                    right_half = binary_search(mid+1, r, target)
                    if right_half:
                        return True
                    return binary_search(l, mid-1, target)
            
        return binary_search(0, len(nums)-1, target)
