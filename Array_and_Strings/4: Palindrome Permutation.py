class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def can_permute_palindrome(self, s: str) -> bool:
        # write your code here

        bit_vector = 0
        for i in range(len(s)):
            ascii = ord(s[i])-ord('a')
            bit_vector ^= (1<<ascii) # toggle

        if bit_vector == 0: # only even counts
            return True
        if bit_vector&(bit_vector-1) == 0: # only one set bit
            return True
        return False
