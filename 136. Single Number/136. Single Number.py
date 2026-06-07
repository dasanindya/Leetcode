#
# Problem: 136. Single Number
# Difficulty: Easy
# Link: https://leetcode.com/problems/single-number/submissions/2025458714/
# Language: python3
# Date: 2026-06-07


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
        
        
