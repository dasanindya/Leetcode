#
# Problem: 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2083981527/
# Language: python3
# Date: 2026-07-27


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lookup = {}
        # curr_len = 0
        # max_len = 0
        # i = 0
        # while i < len(s):
        #     if s[i] in lookup:
        #         if curr_len > max_len:
        #             max_len = curr_len
        #         curr_len = 0
        #         i = lookup[s[i]]+1
        #         lookup = {}
        #     else:
        #         lookup[s[i]] = i
        #         curr_len += 1
        #         i += 1
        # return max(curr_len,max_len)

        # Instead of jumping back and wiping the dictionary, 
        # use a left pointer (left) to mark the start of the current window and 
        # update left whenever a repeating character is found

        lookup = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            # If character is in lookup and inside current window
            if char in lookup and lookup[char] >= left:
                left = lookup[char] + 1

            lookup[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
                

            

        
