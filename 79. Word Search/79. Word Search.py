#
# Problem: 79. Word Search
# Difficulty: Medium
# Link: https://leetcode.com/problems/word-search/submissions/2079743838/
# Language: python3
# Date: 2026-07-24


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])

        def dfs(i,r,c):
        
            if r<0 or c<0 or r>=n_rows or c>=n_cols or board[r][c] != word[i]:
                return False

            if i == len(word)-1:
                return True
            
            # Temporarily mark as visited so we don't reuse this cell
            temp = board[r][c]
            board[r][c] = '#'
            
            found = dfs(i+1,r-1,c) or \
                        dfs(i+1,r+1,c) or \
                        dfs(i+1,r,c-1) or \
                        dfs(i+1,r,c+1)
            # Backtrack: restore the original character
            board[r][c] = temp
            
            return found


        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == word[0] and dfs(0,r,c):
                    return True
        return False

        
