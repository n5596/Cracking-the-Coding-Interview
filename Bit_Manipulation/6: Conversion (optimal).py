class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        xor = start ^ goal
        
        count = 0
        while xor > 0:
            count += 1
            xor = xor&(xor-1) # moving to the next set bit
        return count
