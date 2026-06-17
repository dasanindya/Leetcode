#
# Problem: 55. Jump Game
# Difficulty: Medium
# Link: https://leetcode.com/problems/jump-game/description/
# Language: python3
# Date: 2026-06-17


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_reach = 0
        
        # Greedy approach to track the maximum reachable index as we iterate through the array.
        for i in range(len(nums)):
            # If the current index is further than anything we can reach, we are stuck
            if i > max_reach:
                return False
                
            # Update the furthest position we can reach from this index
            max_reach = max(max_reach, i + nums[i])
            
            # If we can reach or exceed the very last index, we win!
            if max_reach >= len(nums) - 1:
                return True
                
        return True

        
