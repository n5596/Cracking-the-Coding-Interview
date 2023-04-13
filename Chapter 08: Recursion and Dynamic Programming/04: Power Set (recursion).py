class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def recurse(idx, n):
            if idx == n:
                return [set()]
            
            prev_subsets = recurse(idx+1, n)
            
            curr_subsets = []
            for p in prev_subsets:
                # without nums[idx]
                curr_subsets.append(p)
                
                # with nums[idx]
                new_p = copy.copy(p)
                new_p.add(nums[idx])
                curr_subsets.append(new_p)
            return curr_subsets
        
        return recurse(0, len(nums))
