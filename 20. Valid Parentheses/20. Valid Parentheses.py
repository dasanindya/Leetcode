#
# Problem: 20. Valid Parentheses
# Difficulty: Easy
# Link: https://leetcode.com/problems/valid-parentheses/submissions/2024804456/
# Language: python3
# Date: 2026-06-07


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                # closing bracket: stack must be non-empty AND top must match
                if not stack or stack.pop() != pairs[ch]:
                    return False
        return not stack
