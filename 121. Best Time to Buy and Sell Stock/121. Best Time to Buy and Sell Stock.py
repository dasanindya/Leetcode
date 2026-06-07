#
# Problem: 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2024800035/
# Language: python3
# Date: 2026-06-07


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price <= min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit


        
