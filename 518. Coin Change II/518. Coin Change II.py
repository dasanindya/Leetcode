#
# Problem: 518. Coin Change II
# Difficulty: Medium
# Link: https://leetcode.com/problems/coin-change-ii/submissions/2071074939/
# Language: python3
# Date: 2026-07-17


from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        The Crucial Trap: Combinations vs. Permutations
        The most common mistake on this problem is treating it like Coin Change I or Climbing Stairs, 
        which counts permutations (where [1, 2, 1] and [1, 1, 2] are counted as separate ways). 
        Here, we are asked for combinations (where order does not matter; [1, 1, 2] is the same as [1, 2, 1]).

        To avoid duplicates and guarantee we only count unique combinations, 
        we must iterate through the coins in the outer loop, and the target amounts in the inner loop.

        By locking in one coin at a time, we force the combinations to be generated 
        in a non-decreasing order of coin values, ensuring no duplicates are counted.
        '''
        # The number of ways to reach amount i using the current coin 
        # includes all the ways we could make the amount i - coin 
        # (since we can just append the current coin to all of those combinations to reach i).

        # dp[i] will store the number of combinations to make amount i
        dp = [0] * (amount + 1)
        
        # Base case: 1 way to make amount 0 (using no coins)
        dp[0] = 1
        
        # Outer loop: process one coin at a time to prevent duplicate permutations
        for coin in coins:
            # Inner loop: calculate combinations for all amounts from current coin to target amount
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                
        return dp[amount]

        
