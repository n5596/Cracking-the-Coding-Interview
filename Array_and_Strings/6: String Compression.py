class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)
        count = 0
        
        char_count = 0
        j = 0
        for i in range(n):
            char_count += 1
            
            if i == n-1 or chars[i] != chars[i+1]:
                if char_count != 1:
                    char_s = str(char_count)
                    len_char = len(char_s)
                    chars[j] = chars[i]
                    j += 1
                    for k in range(len_char):
                        chars[j+k] = char_s[k]
                    count = 1+len_char
                    j += len_char
                else:
                    chars[j] = chars[i]
                    j += 1
                char_count = 0
                
        return j
