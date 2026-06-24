#
# Problem: 238. Product of Array Except Self
# Difficulty: Medium
# Link: https://leetcode.com/problems/product-of-array-except-self/submissions/2044173533/
# Language: python3
# Date: 2026-06-24


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zerocount = 0
        for n in nums:
            if n!=0:
                product *= n
            else:
                zerocount += 1
        if zerocount>1:
            return [0]*len(nums)
        elif zerocount == 1:
            ret_prod = []
            for n in nums:
                if n!=0:
                    ret_prod.append(0)
                else:
                    ret_prod.append(product)
            return ret_prod
        else:
            ret_prod = []
            for n in nums:
                ret_prod.append(product//n)
            return ret_prod


        
