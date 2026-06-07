#
# Problem: 155. Min Stack
# Difficulty: Medium
# Link: https://leetcode.com/problems/min-stack/
# Language: python3
# Date: 2026-06-07


class MinStack:
    # single stack
    # def __init__(self):
    #     # Each entry is (value, min_so_far_including_this_value)
    #     self.stack = []

    # def push(self, value: int) -> None:
    #     current_min = value if not self.stack else min(value, self.stack[-1][1])
    #     self.stack.append([value, current_min])

    # def pop(self) -> None:
    #     self.stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1][0]

    # def getMin(self) -> int:
    #     return self.stack[-1][1]


    # The two-stack variant
    def __init__(self):
        self.stack = []
        self.mins = []   # parallel stack of running minimums

    def push(self, val) -> None:
        self.stack.append(val)
        if not self.mins or val <= self.mins[-1]: # <= is mandatory, Consider pushing [2, 1, 1]
            self.mins.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
