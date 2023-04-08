class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        def find_multiples5(n):
            count = 0
            
            i = 5
            while n//i > 0:
                count += n//i # find multiples of i are in n
                i *= 5
                
            return count
        
        return find_multiples5(n)
