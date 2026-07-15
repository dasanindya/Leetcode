#
# Problem: 91. Decode Ways
# Difficulty: Medium
# Link: https://leetcode.com/problems/decode-ways/submissions/2067967261/
# Language: python3
# Date: 2026-07-15


class Solution:
    def numDecodings(self, s: str) -> int:
        # similarly to the "Climbing Stairs" problem

        # At any given index i in the string, you have up to two choices:
        # Decode a single digit: Take s[i] if it is not '0' (since '0' alone cannot map to any letter).
        # Decode a two-digit number: Take s[i-1 : i+1] if the combined value is between 10 and 26.
        
        if not s or s[0] == '0':
            return 0
        
        # m0 represents dp[i-2], m1 represents dp[i-1]
        m0 = 1  # Ways to decode empty string
        m1 = 1  # Ways to decode string of length 1 (since s[0] != '0')
        
        for i in range(1, len(s)):
            current = 0
            
            # 1. Single digit step
            if s[i] != '0':
                current += m1
                
            # 2. Two-digit step
            two_digit = int(s[i-1 : i+1])
            if 10 <= two_digit <= 26:
                current += m0
                
            # Update our states for the next iteration
            m0 = m1
            m1 = current
            
            # If at any point we cannot decode further, we can exit early
            if m1 == 0:
                return 0
                
        return m1
        
