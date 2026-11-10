#
# Problem: 376. Wiggle Subsequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/wiggle-subsequence/submissions/2193090665/
# Language: python3
# Date: 2026-11-10


class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        up, down = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
                
        return max(up, down)

        # if not nums:
        #     return 0
            
        # last_diff = 0
        # count = 1
        
        # for i in range(1, len(nums)):
        #     current_diff = nums[i] - nums[i-1]
            
        #     # If the current difference is positive and the last was negative/zero,
        #     # OR the current difference is negative and the last was positive/zero
        #     if (current_diff > 0 and last_diff <= 0) or (current_diff < 0 and last_diff >= 0):
        #         count += 1
        #         last_diff = current_diff
                
        # return count
        
