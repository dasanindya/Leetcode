#
# Problem: 994. Rotting Oranges
# Difficulty: Medium
# Link: https://leetcode.com/problems/rotting-oranges/submissions/2077017618/
# Language: python3
# Date: 2026-07-22


from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Step 1: Initialize queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        # If there are no fresh oranges to begin with, 0 minutes have elapsed
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Step 2: Multi-source BFS
        while queue and fresh_count > 0:
            # Process all nodes at the current minute layer
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is a fresh orange, rot it and add to queue
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
            
            # After processing a full layer, 1 minute has passed
            minutes += 1
            
        # Step 3: Check if all fresh oranges have rotted
        return minutes if fresh_count == 0 else -1
