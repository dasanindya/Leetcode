#
# Problem: 36. Valid Sudoku
# Difficulty: Medium
# Link: https://leetcode.com/problems/valid-sudoku/submissions/2082160801/
# Language: python3
# Date: 2026-07-26


from collections import defaultdict

class Solution:
  def isValidSudoku(self, board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val == ".":
          continue

        box_key = (r // 3, c // 3)

        # Check if digit already exists in row, column, or sub-box
        if val in rows[r] or val in cols[c] or val in boxes[box_key]:
          return False

        # Add digit to trackers
        rows[r].add(val)
        cols[c].add(val)
        boxes[box_key].add(val)

    return True
