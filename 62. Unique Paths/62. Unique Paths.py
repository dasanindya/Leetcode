#
# Problem: 62. Unique Paths
# Difficulty: Medium
# Link: https://leetcode.com/problems/unique-paths/
# Language: python3
# Date: 2026-06-08


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[None for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]

        # # dp[j] = number of paths to reach cell (current_row, j)
        # dp = [1] * n
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[j] += dp[j - 1]
        # return dp[-1]
        
