#
# Problem: 11. Container With Most Water
# Difficulty: Medium
# Link: https://leetcode.com/problems/container-with-most-water/submissions/2070971526/
# Language: python3
# Date: 2026-07-17


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate current width
            width = right - left
            
            # Calculate current height (limited by the shorter bar)
            curr_height = min(height[left], height[right])
            
            # Calculate and record the area if it's the new maximum
            current_area = width * curr_height
            max_water = max(max_water, current_area)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
        
