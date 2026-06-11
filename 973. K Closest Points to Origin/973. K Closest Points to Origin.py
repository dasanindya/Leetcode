#
# Problem: 973. K Closest Points to Origin
# Difficulty: Medium
# Link: https://leetcode.com/problems/k-closest-points-to-origin/submissions/2029195157/
# Language: python3
# Date: 2026-06-11


import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_heap = []
        
        # 1. Initialize the heap with the first K points
        for x, y in points[:k]:
            # Use **2, and skip math.sqrt()
            # Negate the score to simulate a Max-Heap
            dist = -(x**2 + y**2)
            distance_heap.append([dist, [x, y]])
        
        heapq.heapify(distance_heap)

        # 2. Process the remaining points
        for x, y in points[k:]:
            dist = -(x**2 + y**2)
            # distance_heap[0][0] holds the most negative value (farthest point).
            # If the new point's distance is greater (closer to 0 / closer to origin),
            # it means it's closer than our current maximum threshold point.
            if dist > distance_heap[0][0]:
                heapq.heapreplace(distance_heap, [dist, [x, y]])
        
        # Extract the raw coordinate lists from the heap structures
        return [point_info[1] for point_info in distance_heap]


        
