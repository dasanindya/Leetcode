#
# Problem: 155. Min Stack
# Difficulty: Medium
# Link: https://leetcode.com/problems/min-stack/submissions/2024810354/
# Language: python3
# Date: 2026-06-07


class MinStack:

    def __init__(self):
        # Each entry is (value, min_so_far_including_this_value)
        self.stack = []

    def push(self, value: int) -> None:
        current_min = value if not self.stack else min(value, self.stack[-1][1])
        self.stack.append([value, current_min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
