#
# Problem: 704. Binary Search
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-search/
# Language: python3
# Date: 2026-06-07


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Calculate the middle index safely
            mid = (left + right) // 2
            
            # Found the target, return its absolute index
            if nums[mid] == target:
                return mid
            # Target is smaller, discard the right half
            elif nums[mid] > target:
                right = mid - 1
            # Target is larger, discard the left half
            else:
                left = mid + 1
                
        # If left > right, the target does not exist in the array
        return -1

































# class Solution:
#     
