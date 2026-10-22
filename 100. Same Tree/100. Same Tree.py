#
# Problem: 100. Same Tree
# Difficulty: Easy
# Link: https://leetcode.com/problems/same-tree/submissions/2178820225/
# Language: python3
# Date: 2026-10-22


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Base case 1: Both nodes are None
        if not p and not q:
            return True

        # Base case 2: One node is None or values don't match
        if not p or not q or p.val != q.val:
            return False

        # Recursively compare left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



        # def dfs(head):
        #     stack = []
        #     nodes_lst = []
        #     stack.append(head)
            
        #     while len(stack) > 0:
        #         node = stack.pop()
        #         if node: 
        #             stack.append(node.right)
        #             stack.append(node.left)

        #         if node:
        #             nodes_lst.append(node.val)
        #         else:
        #             nodes_lst.append(None)

        #     return nodes_lst

        # p_nodes = dfs(p)
        # q_nodes = dfs(q)
        # #print(p_nodes)
        # #print(q_nodes)

        # if len(p_nodes)!=len(p_nodes):
        #     return False
        # for i in range(len(p_nodes)):
        #     if p_nodes[i] != q_nodes[i]:
        #         return False
        # return True
        
