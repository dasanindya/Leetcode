#
# Problem: 70. Climbing Stairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/climbing-stairs/submissions/2026779426/
# Language: python3
# Date: 2026-06-08


class Solution:
    def climbStairs(self, n: int) -> int:
        step2, step1 = 1, 2 # i-2, i-1 steps
        if n==1:
            return step2
        elif n==2:
            return step1
        else:
            for i in range(3,n+1):
                step = step1 + step2
                step2 = step1
                step1 = step
        return step

        # prev2, prev1 = 1, 1   # ways to reach step 0 and step 1
        # for _ in range(2, n + 1):
        #     prev2, prev1 = prev1, prev1 + prev2
        # return prev1
        
