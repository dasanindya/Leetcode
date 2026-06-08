#
# Problem: 198. House Robber
# Difficulty: Medium
# Link: https://leetcode.com/problems/house-robber/
# Language: python3
# Date: 2026-06-08


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0 # max looting at i-2, i-1
        for num in nums:
            prev2, prev1 = prev1, max(prev2 + num, prev1)
        return prev1        
        
        
        

        
