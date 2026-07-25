#
# Problem: 49. Group Anagrams
# Difficulty: Medium
# Link: https://leetcode.com/problems/group-anagrams/submissions/2080700315/
# Language: python3
# Date: 2026-07-25


#from collections import Counter

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sorted_key = "".join(sorted(s))
            groups[sorted_key].append(s)

        return list(groups.values())



        # return_list = []
        # for s in strs:
        #     if len(return_list)==0:
        #         return_list.append([s])
        #     else:
        #         flag = False
        #         for i in range(len(return_list)):
        #             if Counter(return_list[i][0])==Counter(s):
        #                 flag = True
        #                 break
        #         if flag:
        #             return_list[i].append(s)
        #         else:
        #             return_list.append([s])
        # return return_list
        
