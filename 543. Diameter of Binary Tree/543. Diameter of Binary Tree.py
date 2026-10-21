#
# Problem: 543. Diameter of Binary Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/diameter-of-binary-tree/description/
# Language: python3
# Date: 2026-10-21


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0      # initilize to 0, as can not compare with None and int
        
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            # Recursively get the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Update the global maximum diameter (edges = left_height + right_height)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # Return the height of the current node
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.max_diameter
        
