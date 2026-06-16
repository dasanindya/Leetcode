#
# Problem: 3612. Process String with Special Operations I
# Difficulty: Medium
# Link: https://leetcode.com/problems/process-string-with-special-operations-i/submissions/2034690837/?envType=daily-question&envId=2026-06-16
# Language: python3
# Date: 2026-06-16


class Solution:
    def processStr(self, s: str) -> str:
        result = ''
        for ch in s:
            if ch == '*':
                result = result[:-1]
            elif ch == '#':
                result = result+result
            elif ch == '%':
                result = result[::-1]
            else:
                result += ch
            #print(ch, result)
        return result
        


