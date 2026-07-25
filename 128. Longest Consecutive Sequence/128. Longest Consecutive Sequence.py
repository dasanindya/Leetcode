#
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/submissions/2080826921/
# Language: python3
# Date: 2026-07-25


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_len = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # Ignore duplicates
            elif nums[i] == nums[i - 1] + 1:
                curr += 1
            else:
                max_len = max(max_len, curr)
                curr = 1

        return max(max_len, curr)  # Don't forget the final sequence!
