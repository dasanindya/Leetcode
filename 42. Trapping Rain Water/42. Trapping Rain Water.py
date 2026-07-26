#
# Problem: 42. Trapping Rain Water
# Difficulty: Hard
# Link: https://leetcode.com/problems/trapping-rain-water/submissions/2082017749/
# Language: python3
# Date: 2026-07-26


class Solution:
    def trap(self, height: List[int]) -> int:
        # the water level at left (of max height) is bounded by left_max (regardless of how tall walls further right might be)
        # the water level at right (of max height) is bounded by right_max (regardless of how tall walls further right might be)

        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trapped += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trapped += right_max - height[right]

        return water_trapped

        # # Precomputed Prefix/Suffix Max
        # if not height:
        #     return 0

        # n = len(height)
        # left_max = [0] * n
        # right_max = [0] * n

        # # 1. Fill left_max (Prefix Max)
        # left_max[0] = height[0]
        # for i in range(1, n):
        #     left_max[i] = max(left_max[i - 1], height[i])

        # # 2. Fill right_max (Suffix Max)
        # right_max[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(right_max[i + 1], height[i])

        # # 3. Calculate trapped water
        # water_trapped = 0
        # for i in range(n):
        #     water_trapped += min(left_max[i], right_max[i]) - height[i]

        # return water_trapped
