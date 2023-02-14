class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here

        def sorted_insert(s, val):
            if s == [] or val > s[-1]:
                s.append(val)
            else:
                temp = s.pop()
                sorted_insert(s, val)
                s.append(temp)
            return 
        
        def sort_stack(s):
            if s != []:
                temp = s.pop()
                sort_stack(s)
                sorted_insert(s, temp)
            return
        
        sort_stack(s)
        return
