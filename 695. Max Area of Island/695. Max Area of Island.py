#
# Problem: 695. Max Area of Island
# Difficulty: Medium
# Link: https://leetcode.com/problems/max-area-of-island/submissions/2031037381/
# Language: python3
# Date: 2026-06-12


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        areas = []

        def get_area_using_dfs(i:int, j:int):
            if i<0 or j<0 or i>=rows or j>=cols or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            a1 = get_area_using_dfs(i-1,j)
            a2 = get_area_using_dfs(i+1,j)
            a3 = get_area_using_dfs(i,j-1)
            a4 = get_area_using_dfs(i,j+1)

            return a1+a2+a3+a4+1


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = get_area_using_dfs(i,j)
                    areas.append(area)
        if areas:
            return max(areas)
        else:
            return 0
                
        
