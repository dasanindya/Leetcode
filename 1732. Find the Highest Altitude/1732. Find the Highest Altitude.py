#
# Problem: 1732. Find the Highest Altitude
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-highest-altitude/submissions/2038128244/?envType=daily-question&envId=2026-06-19
# Language: python3
# Date: 2026-06-19


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0
        for g in gain:
            altitude += g
            if altitude > 0:
                highest = max(highest, altitude)
        return highest
        



        
