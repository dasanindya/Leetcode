#
# Problem: 46. Permutations
# Difficulty: Medium
# Link: https://leetcode.com/problems/permutations/
# Language: python3
# Date: 2026-07-24


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # divide nums into two parts: processed elements on the left, and available elements on the right.
        result = []
        
        def backtrack(first=0):
            # Base Case: all integers are placed
            if first == len(nums):
                result.append(nums.copy())
                return
            
            for i in range(first, len(nums)):
                # Swap current element with the first available position
                nums[first], nums[i] = nums[i], nums[first]
                
                # Recursively complete the rest of the permutation
                backtrack(first + 1)
                
                # Backtrack: swap back to restore original state
                nums[first], nums[i] = nums[i], nums[first]
                
        backtrack(0)
        return result
        
