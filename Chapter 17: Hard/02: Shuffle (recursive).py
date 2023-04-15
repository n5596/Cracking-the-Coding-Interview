class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.curr = nums.copy()

    def reset(self) -> List[int]:
        self.curr = self.nums.copy()
        return self.curr

    def recurse(self, idx):
        if idx == 0:
            return 
        
        self.recurse(idx-1)
        k = random.randint(0, idx)
        
        self.curr[idx], self.curr[k] = self.curr[k], self.curr[idx]
        return 
        
    def shuffle(self) -> List[int]:
        self.recurse(len(self.curr)-1)
        return self.curr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
