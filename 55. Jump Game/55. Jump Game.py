#
# Problem: 55. Jump Game
# Difficulty: Medium
# Link: https://leetcode.com/problems/jump-game/submissions/2032229550/
# Language: python3
# Date: 2026-06-14


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reach = 0
        
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

        
