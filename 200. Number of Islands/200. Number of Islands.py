#
# Problem: 200. Number of Islands
# Difficulty: Medium
# Link: https://leetcode.com/problems/number-of-islands/submissions/2030554361/
# Language: python3
# Date: 2026-06-12


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r: int, c: int):

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            grid[r][c] = '0'
            
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        numlands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    numlands += 1
                    dfs(r, c)
                    
        return numlands
