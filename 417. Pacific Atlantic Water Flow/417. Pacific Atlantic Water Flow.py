#
# Problem: 417. Pacific Atlantic Water Flow
# Difficulty: Medium
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/submissions/2198947095/
# Language: python3
# Date: 2026-11-18


from typing import List


class Solution:

  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    if not heights or not heights[0]:
      return []

    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r: int, c: int, visited: set, prev_height: int) -> None:
      # Out of bounds, already visited, or water cannot flow uphill from prev_height
      if (
          r < 0
          or r >= rows
          or c < 0
          or c >= cols
          or (r, c) in visited
          or heights[r][c] < prev_height
      ):
        return

      visited.add((r, c))

      # Explore 4 directions
      dfs(r + 1, c, visited, heights[r][c])
      dfs(r - 1, c, visited, heights[r][c])
      dfs(r, c + 1, visited, heights[r][c])
      dfs(r, c - 1, visited, heights[r][c])

    # Top and bottom edges
    for c in range(cols):
      dfs(0, c, pacific, heights[0][c])
      dfs(rows - 1, c, atlantic, heights[rows - 1][c])

    # Left and right edges
    for r in range(rows):
      dfs(r, 0, pacific, heights[r][0])
      dfs(r, cols - 1, atlantic, heights[r][cols - 1])

    # Cells reachable by both oceans
    return [
        [r, c]
        for r in range(rows)
        for c in range(cols)
        if (r, c) in pacific and (r, c) in atlantic
    ]
