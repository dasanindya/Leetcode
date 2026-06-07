#
# Problem: 704. Binary Search
# Difficulty: Easy
# Link: https://leetcode.com/problems/binary-search/submissions/2025291636/
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

    # # recursion
    # def search(self, nums: list[int], target: int) -> int:
    #     # Helper function tracking the explicit boundary pointers
    #     def binary_search(left: int, right: int) -> int:
    #         # Base Case: Target is not present
    #         if left > right:
    #             return -1
            
    #         mid = (left + right) // 2
            
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] > target:
    #             return binary_search(left, mid - 1) # Search left
    #         else:
    #             return binary_search(mid + 1, right) # Search right

    #     return binary_search(0, len(nums) - 1)

































# class Solution:
#     
