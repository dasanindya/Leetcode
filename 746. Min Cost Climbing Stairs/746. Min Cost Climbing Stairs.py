#
# Problem: 746. Min Cost Climbing Stairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/min-cost-climbing-stairs/submissions/2026774899/
# Language: python3
# Date: 2026-06-08


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost2, cost1 = cost[0] , cost[1] # cost at i-2 and i-1
        for c in cost[2:]:
            cost3 = min(cost2+c, cost1+c)
            cost2 = cost1
            cost1 = cost3
        return min(cost1,cost2)

        # prev2, prev1 = 0, 0   # min cost to reach step i-2 and step i-1
        # for i in range(2, len(cost) + 1):
        #     prev2, prev1 = prev1, min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        # return prev1
        
