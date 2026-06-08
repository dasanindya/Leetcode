#
# Problem: 53. Maximum Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-subarray/submissions/2026803290/
# Language: python3
# Date: 2026-06-08


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = best = nums[0]
        for num in nums[1:]:
            current = max(num, current + num)
            best = max(best, current)
        return best

        
