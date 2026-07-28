#
# Problem: 424. Longest Repeating Character Replacement
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/submissions/2083997969/
# Language: python3
# Date: 2026-07-28


class Solution:

  def characterReplacement(self, s: str, k: int) -> int:
    count = {}
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
      # Add current character to window frequency map
      count[s[right]] = count.get(s[right], 0) + 1

      # Track max frequency within current window
      max_freq = max(max_freq, count[s[right]])

      # Window size - max_freq = number of replacements needed
      # If replacements > k, shrink window from left
      if (right - left + 1) - max_freq > k:
        count[s[left]] -= 1
        left += 1

      max_len = max(max_len, right - left + 1)

    return max_len
