#
# Problem: 1143. Longest Common Subsequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-common-subsequence/submissions/2035780757/
# Language: python3
# Date: 2026-06-17


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # m, n = len(text1), len(text2)

        # # Initialize the entire grid with 0s. 
        # # This automatically covers our base cases (first row and first column = 0)
        # dp = [[0] * (n + 1) for _ in range(m + 1)]

        # # Iterate through both strings
        # for i in range(m):
        #     for j in range(n):
        #         if text1[i] == text2[j]:
        #             # Match found: look diagonally back and add 1
        #             dp[i + 1][j + 1] = 1 + dp[i][j]
        #         else:
        #             # No match: take the best result from either dropping a char from text1 or text2
        #             dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        # return dp[m][n]

        m, n = len(text1), len(text2)
        
        # Only keep track of the previous row and current row
        prev_row = [0] * (n + 1)
        
        for i in range(m):
            curr_row = [0] * (n + 1)
            for j in range(n):
                if text1[i] == text2[j]:
                    curr_row[j + 1] = 1 + prev_row[j]
                else:
                    curr_row[j + 1] = max(prev_row[j + 1], curr_row[j])
            prev_row = curr_row  # Move down to the next row
            
        return prev_row[n]
        




        
