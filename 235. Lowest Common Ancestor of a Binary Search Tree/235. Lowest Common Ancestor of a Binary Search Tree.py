#
# Problem: 235. Lowest Common Ancestor of a Binary Search Tree
# Difficulty: Medium
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/2058619006/
# Language: python3
# Date: 2026-07-07


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # The lowest common ancestor between two nodes p and q is defined as 
        # the deepest (lowest) node in the tree that has both p and q as descendants.
        
        current = root
        
        while current:
            # If both target values are smaller than current, move left
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both target values are larger than current, move right
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # We found the split point or a direct match!
            else:
                return current
