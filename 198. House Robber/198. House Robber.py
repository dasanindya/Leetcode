#
# Problem: 198. House Robber
# Difficulty: Medium
# Link: https://leetcode.com/problems/house-robber/submissions/2066044888/
# Language: python3
# Date: 2026-07-13


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        
        m0 = nums[0]
        m1 = max(nums[0], nums[1])  # important: Account for skipping the 2nd house
        
        for m in nums[2:]:
            max_amount = max(m0 + m, m1)
            m0 = m1
            m1 = max_amount
            
        return m1


        # prev2, prev1 = 0, 0 # max looting at i-2, i-1
        # for num in nums:
        #     prev2, prev1 = prev1, max(prev2 + num, prev1)
        # return prev1        
        
        
        

        
