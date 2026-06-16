#
# Problem: 21. Merge Two Sorted Lists
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/2034910893/
# Language: python3
# Date: 2026-06-16


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            # Combining less-than and equal-to cases handles duplicates 
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # CRITICAL: Always advance the tail pointer after an attachment
            tail = tail.next
            
        # Efficient $O(1)$ cleanup: Just stitch the entire remaining chain at once
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next
        
        
        # dummy = ListNode(0)
        # tail = dummy

        # while list1 and list2:
        #     if list1.val > list2.val:
        #         tail.next = list2
        #         list2 = list2.next

        #         tail = tail.next
        #     elif list1.val < list2.val:
        #         tail.next = list1
        #         list1 = list1.next

        #         tail = tail.next
        #     else:
        #         tail.next = list1
        #         list1 = list1.next
        #         tail = tail.next
        #         tail.next = list2
        #         list2 = list2.next
        #         tail = tail.next
        # while list1:
        #     tail.next = list1
        #     list1 = list1.next
        #     tail = tail.next
        # while list2:
        #     tail.next = list2
        #     list2 = list2.next
        #     tail = tail.next
        
        # return dummy.next

