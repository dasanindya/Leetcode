#
# Problem: 167. Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/2034977089/
# Language: python3
# Date: 2026-06-16


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # second_num_list = []
        # for i in range(len(numbers)):
        #     sec_num = target - numbers[i]
        #     if sec_num in numbers:
        #         j =  numbers.index(sec_num) 
        #         if i == j and numbers[i] == numbers[i+1]: # same element twice
        #             return [i+1,j+2]
        #         if i != j:
        #             return [i+1,j+1]
        # return []

        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Problem requires 1-based indexing
                return [left + 1, right + 1]
                
            elif current_sum < target:
                # Sum is too small, move left pointer forward to get a larger value
                left += 1
                
            else:
                # Sum is too large, move right pointer backward to get a smaller value
                right -= 1
                
        return []  # Fallback, though the problem guarantees exactly one solution exists
