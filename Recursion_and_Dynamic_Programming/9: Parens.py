class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        all_combos = []
        
        def recurse(curr_s, left_rem, right_rem):
            if left_rem < 0 or right_rem < 0:
                return
            elif left_rem == 0 and right_rem == 0:
                all_combos.append(curr_s)
                return
            
            if left_rem > right_rem: # invalid
                return
            
            recurse(curr_s+'(', left_rem-1, right_rem)
            recurse(curr_s+')', left_rem, right_rem-1)
            return
        
        recurse('', n, n)
        return all_combos
