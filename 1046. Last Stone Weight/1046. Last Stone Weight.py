#
# Problem: 1046. Last Stone Weight
# Difficulty: Easy
# Link: https://leetcode.com/problems/last-stone-weight/submissions/2029169070/
# Language: python3
# Date: 2026-06-11


import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq support minheap, invert signs using a list comprehension to simulate a Max-Heap
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Pop the two heaviest stones (negate to make them positive)
            x = -heapq.heappop(heap)  # Heaviest
            y = -heapq.heappop(heap)  # Second heaviest
            
            if x != y:
                # x is larger than y, so (x - y) is the positive remaining weight.
                # We push it back as a negative number to maintain our Max-Heap simulation.
                heapq.heappush(heap, -(x - y))
                
        # Return the last stone's weight, or 0 if none are left
        return -heap[0] if heap else 0
