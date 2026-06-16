#
# Problem: 206. Reverse Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-linked-list/submissions/2034778480/
# Language: python3
# Date: 2026-06-16


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # 1. Save the next node's reference before breaking the link
            curr.next = prev  # 2. Reverse the current node's pointer to face backward
            prev = curr       # 3. Move the 'prev' pointer forward to the current node
            curr = nxt        # 4. Move the 'curr' pointer forward to the saved next node
            
        return prev  # 'prev' will be standing at the new head of the reversed list
        
        
