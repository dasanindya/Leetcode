#
# Problem: 1344. Angle Between Hands of a Clock
# Difficulty: Medium
# Link: https://leetcode.com/problems/angle-between-hands-of-a-clock/submissions/2038038573/?envType=daily-question&envId=2026-06-18
# Language: python3
# Date: 2026-06-18


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_in_hour = minutes/5
        #print("min_in_hour", min_in_hour)
        hour_angle = (hour + (minutes/60)) * 30
        #print("hour_angle", hour_angle)
        min_angle = min_in_hour * 30
        #print("min_angle", min_angle)
        angle = abs(min_angle-hour_angle)
        #print("angle", angle)
        angle = min(angle, 360-angle)
        return angle
        
