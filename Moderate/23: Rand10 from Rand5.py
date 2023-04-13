# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            v1, v2 = rand7(), rand7()
            
            val = 7*(v1-1)+v2
            # v1-1 ensures that val starts at 1
            
            if val <= 40:
                return (val%10)+1
