#
# Problem: 1840. Maximum Building Height
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximum-building-height/submissions/2039313311/?envType=daily-question&envId=2026-06-20
# Language: python3
# Date: 2026-06-20


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        '''
        Coordinate Compression (Two-Pass DP): Instead of keeping track of all 1 billion buildings individually, we only need to care about the restriction checkpoints themselves. The buildings in between checkpoints will naturally form an upside-down "V" shape (climbing up by 1 and then climbing down by 1) to reach their maximum possible heights.
        '''

        # 1. Add our natural boundary conditions as checkpoints
        # Building 1 must have a height of 0. Building n has no initial upper bound (set to n-1).
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        # Sort restrictions by building ID
        restrictions.sort(key=lambda x: x[0])
        m = len(restrictions)
        
        # 2. Left-to-Right Pass: Clamp heights based on left neighbors
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            # Max height is capped by left height + horizontal distance
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
            
        # 3. Right-to-Left Pass: Clamp heights based on right neighbors
        for i in range(m - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            # Max height is capped by right height + horizontal distance
            # Based only on the height restriction of my right neighbor (h2), what is the absolute highest peak I (h1) could possibly reach?
            '''
            Because building i's final allowed height is limited by the tighter of two constraints:Its own original restriction (h1). The maximum height it could possibly climb to given how far away it is from its right neighbor (h2 + distance).
            '''
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
            
        # 4. Calculate the maximum peak between every adjacent pair of restrictions
        max_height = 0
        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            
            # The maximum height reachable between two restricted coordinates
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
            
        return max_height
        
