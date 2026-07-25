#
# Problem: 347. Top K Frequent Elements
# Difficulty: Medium
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Language: python3
# Date: 2026-07-25


from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort Approach
        count = Counter(nums)
        # Index represents frequency (max frequency is len(nums))
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []
        # Iterate backwards from highest possible frequency
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result


        # # Min-Heap Solution
        # count = Counter(nums)
        # heap = []

        # for num, freq in count.items():
        #     heapq.heappush(heap, (freq, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)  # Evict the lowest frequency element

        # return [num for freq, num in heap]
