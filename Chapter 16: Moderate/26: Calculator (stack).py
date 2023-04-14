class Solution:
    def calculate(self, s: str) -> int:
        
        num_stack, op_stack = [], []
        priority = {"+":1,"-":1,"*":2,"/":2, "BLANK":0}
        
        def calculate_op(v1, v2, op):
            if op == "+":
                return v1+v2
            elif op == "-":
                return v1-v2
            elif op == "*":
                return v1*v2
            else:
                return v1//v2
            
        def check_collapse(c):
            
            
            while op_stack != [] and len(num_stack) >= 2 and priority[c] <= priority[op_stack[-1]]: # collapse stack
                op = op_stack.pop()
                
                v2 = num_stack.pop()
                v1 = num_stack.pop()
                    
                result = calculate_op(v1, v2, op)
                num_stack.append(result)
                
            op_stack.append(c)
            return
        
        s = s.strip()
        
        curr_num = 0
        n = len(s)
        
        for i in range(n):
            c = s[i]
            if c  == " ":
                continue
            elif c in "0123456789":
                curr_num = curr_num*10+ord(c)-ord('0')
                
                if i == n-1:
                    num_stack.append(curr_num)
            else:
                
                num_stack.append(curr_num)
                curr_num = 0
                
                check_collapse(c)
                
        check_collapse("BLANK")
        return num_stack[0]
