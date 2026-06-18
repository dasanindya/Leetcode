#
# Problem: 3614. Process String with Special Operations II
# Difficulty: Hard
# Link: https://leetcode.com/problems/process-string-with-special-operations-ii/submissions/2037331530/?envType=daily-question&envId=2026-06-17
# Language: python3
# Date: 2026-06-18




class Solution:
    def processStr(self, s: str, k: int) -> str:
        # result = ''
        # for ch in s:
            
        #     if ch == '*':
        #         if len(result) >= 1:
        #             result = result[:-1]
        #     elif ch == '#':
        #         result = result+result
        #     elif ch == '%':
        #         result = result[::-1]
        #     else:
        #         result +=  ch
        #     #print(ch, result)
        # if k>len(result)-1:
        #     return '.'
        # return result[k]


        # algorithm simulates the transformations mathematically by tracking the string's length forward, and then retroactively mapping the index k backward.
        l = 0
        for c in s:
            if c.islower(): 
                l += 1
            elif c == '*' and l: 
                l -= 1
            elif c == '#': 
                l *= 2
            elif c == '%': 
                pass
                
        if k >= l: 
            return '.'

        # reversed(s) over s[::-1] -> reversed Returns an iterator, 
        # O(1) - Extremely low memory footprint
        for c in reversed(s):
            if c.islower():
                if k == l - 1: 
                    return c
                l -= 1
            elif c == '*': 
                l += 1
            elif c == '#':
                l //= 2
                if k >= l: 
                    k -= l
            elif c == '%': 
                k = l - 1 - k

        
