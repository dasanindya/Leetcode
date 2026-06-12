#
# Problem: 78. Subsets
# Difficulty: Medium
# Link: https://leetcode.com/problems/subsets/submissions/2030325125/
# Language: python3
# Date: 2026-06-12


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int):
            # Base Case: If we've made a decision for all elements in current branch
            if i >= len(nums):
                res.append(subset.copy())  # Append a copy, not the reference
                return
            
            # Decision 1: INCLUDE nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            # Decision 2: EXCLUDE nums[i] (Backtrack)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

        
