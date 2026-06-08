#
# Problem: 74. Search a 2D Matrix
# Difficulty: Medium
# Link: https://leetcode.com/problems/search-a-2d-matrix/submissions/2026506698/
# Language: python3
# Date: 2026-06-08


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return None
        
        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows*cols-1

        while lo <= hi:
            mid = (lo+hi)//2
            
            r = mid//cols
            c = mid%cols
            # r, c = divmod(mid, cols)

            val = matrix[r][c]

            if val == target:
                return True
            elif val>target:
                hi = mid-1
            else: #val<target
                lo = mid+1

        return False


        
