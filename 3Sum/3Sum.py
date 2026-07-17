#
# Problem: 3Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/3sum/submissions/2070962526/
# Language: python3
# Date: 2026-07-17


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # lock in one number and turn the remaining problem into a classic Two Sum II (Two-Pointer) problem
        res = []
        nums.sort()  # Step 1: Sort the array
        
        for i in range(len(nums)):
            # Optimization: If the pivot is positive, we can't sum to 0 anymore
            if nums[i] > 0:
                break
                
            # Optimization: Skip duplicate pivot elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 2: Initialize Two Pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Update pointers and skip duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res
        
