class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        all_subsets = []
        
        max_binary = pow(2, len(nums))
        
        for i in range(max_binary):
            curr_set = set()
            temp = i 
            
            idx = 0
            while temp > 0:
                if temp & 1 == 1:
                    curr_set.add(nums[idx])
                idx += 1
                temp >>= 1
                
            all_subsets.append(curr_set)
        return all_subsets
