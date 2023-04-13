class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0:
            return "Zero"
        
        smalls = ["*", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen","Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["*", "*", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        bigs = ["Thousand", "Million", "Billion"]
        
        def convert_chunk(n, chunk_idx=-1):
            if n == 0:
                return ""
            
            new_s = ""
            if n >= 100:
                new_s += smalls[n//100]+" Hundred"
                
            n = n % 100
            
            if n >= 10 and n < 20:
                new_s += " " + smalls[n]
            else:
                
                if n >= 20:
                    new_s += " " + tens[n//10]  
                    n = n % 10
            
                if n != 0:
                    new_s += " " + smalls[n]
            
            if chunk_idx >= 0:
                new_s += " " + bigs[chunk_idx]
                
            new_s = new_s.strip()
            return new_s
            
        s = ""
            
        if num >= 10**9:
            s += " " + convert_chunk(num//(10**9), 2)
            num = num % 10**9
        
        if num >= 10**6:
            s += " " + convert_chunk(num//(10**6), 1)
            num = num % 10**6

        if num >= 10**3:
            s += " " + convert_chunk(num//(10**3), 0)
            num = num % 10**3
        
        s += " " + convert_chunk(num)
            
        s = s.strip()
        return s
