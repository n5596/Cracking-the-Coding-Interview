#User function Template for python3

class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here

        odd_bits = n & 0xAAAAAAAA # 0xAAAAAAAA is the mask to get odd bits
        even_bits = n & 0x55555555 # 0x55555555 is the mask to get even bits
        
        shifted_odd = odd_bits >> 1
        shifted_even = even_bits << 1
        output = shifted_odd | shifted_even
        return output
