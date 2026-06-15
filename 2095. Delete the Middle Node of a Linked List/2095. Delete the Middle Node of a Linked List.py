#
# Problem: 2095. Delete the Middle Node of a Linked List
# Difficulty: Medium
# Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=daily-question&envId=2026-06-15
# Language: python3
# Date: 2026-06-15


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return None

        # slow , fast = head, head

        # prev = None
        # while fast.next and fast.next.next:
        #     prev = slow
        #     slow = slow.next
        #     fast = fast.next.next
        # if fast.next and not fast.next.next:
        #     prev = slow
        #     slow = slow.next
        
        # prev.next = slow.next
        # return head
        #----------------------------------

        if not head or not head.next:
            return None

        prev = None
        slow = head
        fast = head

        # Standard slow/fast loop. When fast reaches the end, slow is exactly at the middle.
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Skip the middle node entirely to delete it.
        prev.next = slow.next
        
        return head

        

        
        


        
