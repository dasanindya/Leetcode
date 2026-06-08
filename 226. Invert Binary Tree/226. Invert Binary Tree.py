#
# Problem: 226. Invert Binary Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/invert-binary-tree/submissions/2026471544/
# Language: python3
# Date: 2026-06-08


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

## What LeetCode does behind the scenes
# from collections import deque

# def build_tree(values):
#     if not values:
#         return None
#     root = TreeNode(values[0])
#     queue = deque([root])
#     i = 1
#     while queue and i < len(values):
#         node = queue.popleft()
#         # Left child
#         if i < len(values) and values[i] is not None:
#             node.left = TreeNode(values[i])
#             queue.append(node.left)
#         i += 1
#         # Right child
#         if i < len(values) and values[i] is not None:
#             node.right = TreeNode(values[i])
#             queue.append(node.right)
#         i += 1
#     return root
