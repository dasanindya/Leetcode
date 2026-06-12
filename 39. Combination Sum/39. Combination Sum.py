#
# Problem: 39. Combination Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/combination-sum/submissions/2030340574/
# Language: python3
# Date: 2026-06-12


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        current = []
        result = []
        
        def dfs(i: int):
            if sum(current) == target:
                result.append(current[:])
                return
            # Important: out-of-bounds guard clause (i >= len(candidates))
            elif sum(current) > target or i >= len(candidates):
                return

            # Decision 1: Re-use the current element
            current.append(candidates[i])
            dfs(i)

            # Decision 2: Skip the current element and move forward
            current.pop()
            dfs(i+1)
        
        dfs(0)
        return result
