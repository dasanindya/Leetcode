#
# Problem: 572. Subtree of Another Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/subtree-of-another-tree/
# Language: python3
# Date: 2026-10-22


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        # def isSameTree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        #     # Helper from LeetCode 100: Checks if two trees are identical
        #     if not s and not t:
        #         return True
        #     if not s or not t or s.val != t.val:
        #         return False
        #     return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        # if not subRoot:
        #     return True
        # if not root:
        #     return False

        # # Check if trees match starting from the current root node
        # if isSameTree(root, subRoot):
        #     return True

        # # Otherwise, check the left and right subtrees of the main tree
        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)




        def dfs(head):
            stack = [head]
            nodes_lst = []
            while stack:
                node = stack.pop()
                if node:
                    stack.append(node.right)
                    stack.append(node.left)
                    # Add a unique prefix '#' to prevent integer prefix collisions (e.g., 12 vs 2)
                    nodes_lst.append(f"#{node.val}")
                else:
                    nodes_lst.append("#NA")
            return "".join(nodes_lst)

        root_str = dfs(root)
        subroot_str = dfs(subRoot)

        return subroot_str in root_str
        
