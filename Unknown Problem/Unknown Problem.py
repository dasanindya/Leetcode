#
# Problem: Unknown Problem
# Difficulty: Medium
# Link: https://leetcode.com/problems/balanced-binary-tree/submissions/2177883954/
# Language: python3
# Date: 2026-10-21


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if abs(left_height-right_height)>1 or left_height == -1 or right_height == -1:\
            # return a sentinel value (like -1) to immediately short-circuit and propagate the failure all the way up, avoiding unnecessary computations.
                return -1

            return 1+max(left_height,right_height)
        
        return dfs(root) != -1
        
