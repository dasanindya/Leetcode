#
# Problem: 22. Generate Parentheses
# Difficulty: Medium
# Link: https://leetcode.com/problems/generate-parentheses/submissions/2079521119/
# Language: python3
# Date: 2026-07-24


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
    
        def backtrack(current_str: str, open_count: int, close_count: int):
            # Base case: reached valid combination of length 2*n
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Choice 1: Add an opening parenthesis if we haven't reached 'n'
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
                
            # Choice 2: Add a closing parenthesis if it wouldn't exceed open ones
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return result
        


