#
# Problem: 53. Maximum Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-subarray/submissions/2048362030/
# Language: python3
# Date: 2026-06-28


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Step 1: Initialize tracking states with the first element
        curr_sum = nums[0]
        max_sum = nums[0]
        
        # Step 2: Traverse through the rest of the array
        for num in nums[1:]:
            # Core Decision: Should we extend the old subarray or start fresh from 'num'?
            curr_sum = max(num, curr_sum + num)
            
            # Record the highest sub-calculation peak found
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
        
