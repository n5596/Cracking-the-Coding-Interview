class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        combos = []
        if digits == "":
            return combos
        
        def find_letters(c):
            
            if c == "2":
                return "abc"
            elif c == "3":
                return "def"
            elif c == "4":
                return "ghi"
            elif c == "5":
                return "jkl"
            elif c == "6":
                return "mno"
            elif c == "7":
                return "pqrs"
            elif c == "8":
                return "tuv"
            elif c == "9":
                return "wxyz"
            
        def recurse(s, idx):
            if idx == len(digits):
                combos.append(s)
                return
            
            letters = find_letters(digits[idx])
            
            for c in letters:
                recurse(s+c, idx+1)
                
            return 
            
        recurse("", 0)
        return combos
