#
# Problem: 213. House Robber II
# Difficulty: Medium
# Link: https://leetcode.com/problems/house-robber-ii/submissions/2035747611/
# Language: python3
# Date: 2026-06-17


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: If there is only one house, just rob it
        if len(nums) == 1:
            return nums[0]
            
        # Helper function for standard House Robber I (linear line of houses)
        def rob_linear(houses: List[int]) -> int:
            prev2, prev1 = 0, 0
            for money in houses:
                # The max money at the current house is either:
                # 1. Skip this house (keep prev1)
                # 2. Rob this house + money from 2 houses ago (prev2 + money)
                curr = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = curr
            return prev1

        # The answer is the best option between skipping the last house 
        # or skipping the first house
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
