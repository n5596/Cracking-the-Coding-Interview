### https://leetcode.com/problems/sum-of-two-integers/discuss/1440775/Python-solution-with-comments-works-with-negative-arguments

class Solution:    
    def getSum(self, a: int, b: int) -> int:
        
        # Move a and b into the range [0, 4000] by taking them mod 4001
        # Since -1000 <= a,b <= 1000, we have -2000 <= a + b <= 2000
        
        UPPER_BOUND = 4001
        a = a % UPPER_BOUND
        b = b % UPPER_BOUND
        
        def add(a, b):
            if b == 0:
                return a
            
            sum_val = a ^ b 
            carry = (a & b) << 1
            
            return add(sum_val, carry)
        
        c = add(a, b)
        c = c % UPPER_BOUND
        
        # If c > 2000, this means that the result is negative as a,b are both less than 2000. 
        # ~0 = -1
        
        if c > 2000:
            c = ((~0) *c) % UPPER_BOUND
            c *= ~0
        return c
