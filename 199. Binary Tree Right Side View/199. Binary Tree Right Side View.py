#
# Problem: 199. Binary Tree Right Side View
# Difficulty: Medium
# Link: https://leetcode.com/problems/binary-tree-right-side-view/submissions/2179905917/
# Language: python3
# Date: 2026-10-23


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # The last node in this level is visible from the right side
                if i == level_size - 1:
                    result.append(node.val)

                # Enqueue children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
        
