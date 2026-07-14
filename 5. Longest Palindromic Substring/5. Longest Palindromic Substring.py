#
# Problem: 5. Longest Palindromic Substring
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-palindromic-substring/submissions/2067260133/
# Language: python3
# Date: 2026-07-14


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Base case: a single character is always a palindrome of length 1
        start_idx = 0
        pal_len = 1
        
        for i in range(1, len(s)):
            # Check 1: Can we extend the palindrome length by 2?
            # This looks at a substring of length (pal_len + 2) ending at index i
            if i - pal_len - 1 >= 0:
                sub = s[i - pal_len - 1 : i + 1]
                if sub == sub[::-1]:
                    start_idx = i - pal_len - 1
                    pal_len += 2
                    continue  # Move to next character if we found a longer one
            
            # Check 2: Can we extend the palindrome length by 1?
            # This looks at a substring of length (pal_len + 1) ending at index i
            if i - pal_len >= 0:
                sub = s[i - pal_len : i + 1]
                if sub == sub[::-1]:
                    start_idx = i - pal_len
                    pal_len += 1
                    
        return s[start_idx : start_idx + pal_len]
