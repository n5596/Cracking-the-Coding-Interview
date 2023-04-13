class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        hashmap = {}
        operations = 0
        
        for val in nums:
            if hashmap.get(k-val, 0) > 0:
                hashmap[k-val] -= 1
                operations += 1
            else:
                hashmap[val] = hashmap.get(val, 0)+1 # this value is now unpaired
                
        return operations
