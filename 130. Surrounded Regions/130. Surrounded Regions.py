#
# Problem: 130. Surrounded Regions
# Difficulty: Medium
# Link: https://leetcode.com/problems/surrounded-regions/submissions/2077000646/
# Language: python3
# Date: 2026-07-22


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row_len, col_len = len(board), len(board[0])
        current_set =  set()
        processed_set = set()

        def dfs(r,c):
            if r<0 or c<0 or r>=row_len or c>=col_len or board[r][c]=="X" or ((r,c) in current_set) or ((r,c) in processed_set):
                return
            current_set.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        def update_region(index_set):
            for index in index_set:
                if index[0] == 0 or index[1] == 0 or index[0] == row_len-1 or index[1] == col_len-1:
                    return
            for index in index_set:
                board[index[0]][index[1]] = "X"
                
        for i in range(row_len):
            for j in range(col_len):
                processed_set.update(current_set)
                update_region(current_set)
                #print(current_set)
                current_set = set()
                dfs(i,j)
        

        
