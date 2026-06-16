#
# Problem: 125. Valid Palindrome
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-palindrome/submissions/2034951662/
# Language: python3
# Date: 2026-06-16


import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = re.sub(r'[^A-Za-z0-9]', '', s)
        # s = s.lower()
        # return s == s[::-1]

        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True
