#
# Problem: 309. Best Time to Buy and Sell Stock with Cooldown
# Difficulty: Medium
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/2071042937/
# Language: python3
# Date: 2026-07-17


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp hashmap to store (index, buying_state) -> max_profit
        dp = {}  
        
        def dfs(i: int, buying: bool) -> int:
            # Base Case: If we go out of bounds, no more transactions can be made
            if i >= len(prices):
                return 0
                
            # If we have already calculated the max profit for this state, return it
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            # Decision 1: Do nothing (Cooldown/Rest) and move to the next day
            cooldown = dfs(i + 1, buying)
            
            if buying:
                # Decision 2a: Buy today (subtract cost) and shift state to "not buying" for tomorrow
                buy = dfs(i + 1, False) - prices[i]
                # Cache the maximum profit between buying vs resting
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # Decision 2b: Sell today (add gain) and shift state to "buying" after a 1-day cooldown (i + 2)
                sell = dfs(i + 2, True) + prices[i]
                # Cache the maximum profit between selling vs resting
                dp[(i, buying)] = max(sell, cooldown)
                
            return dp[(i, buying)]
            
        # Start search on day 0, with 'buying' state set to True
        return dfs(0, True)
