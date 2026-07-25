#
# Problem: 1. Two Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/two-sum/submissions/2080682124/
# Language: python3
# Date: 2026-07-25


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Map value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []
            
