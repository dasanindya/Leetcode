#
# Problem: 133. Clone Graph
# Difficulty: Medium
# Link: https://leetcode.com/problems/clone-graph/submissions/2030540774/
# Language: python3
# Date: 2026-06-12


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
            
        # Change to tracking Node objects rather than integer values for stability
        visited_nodes = {}
        
        def dfs(current_node):
            if current_node is None: 
                return None
                
            # If already cloned, safely return it to break graph cycles
            if current_node in visited_nodes:
                return visited_nodes[current_node]
                
            # 1. Create the skeleton clone node right away
            new_node = Node(val=current_node.val)
            
            # 2. CRITICAL: Register the clone in the map immediately BEFORE exploring neighbors
            # This ensures that if any downstream neighbor circles back to this node, the base case can instantly catch it and return the reference.
            visited_nodes[current_node] = new_node
            
            # 3. Now it is completely safe to populate neighbors recursively
            if current_node.neighbors: 
                new_node.neighbors = [dfs(neighbor) for neighbor in current_node.neighbors]
            else:
                new_node.neighbors = [] 
                
            return new_node
            
        return dfs(node)


        
