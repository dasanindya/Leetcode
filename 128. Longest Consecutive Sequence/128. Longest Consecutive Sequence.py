#
# Problem: 128. Longest Consecutive Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Language: python3
# Date: 2026-07-26


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            # Only start counting if 'num' is the FIRST element of a sequence
            if num - 1 not in num_set:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1

                max_len = max(max_len, curr_streak)

        return max_len

        # if not nums:
        #     return 0

        # nums.sort()
        # max_len = 1
        # curr = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         continue  # Ignore duplicates
        #     elif nums[i] == nums[i - 1] + 1:
        #         curr += 1
        #     else:
        #         max_len = max(max_len, curr)
        #         curr = 1

        # return max(max_len, curr)  # Don't forget the final sequence!
