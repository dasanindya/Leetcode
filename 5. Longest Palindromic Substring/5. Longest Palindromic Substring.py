#
# Problem: 5. Longest Palindromic Substring
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-palindromic-substring/submissions/2067260928/
# Language: python3
# Date: 2026-07-14


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            # Expand outwards as long as characters match and boundaries are valid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length palindromes (center is s[i])
            len1 = expand_around_center(i, i)
            # Case 2: Even length palindromes (center is between s[i] and s[i+1])
            len2 = expand_around_center(i, i + 1)
            
            # Find the max length from this center
            max_len = max(len1, len2)
            
            # Update the absolute longest bounds if a larger one is found
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]
