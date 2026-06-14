#
# Problem: 2130. Maximum Twin Sum of a Linked List
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/submissions/2032408551/?envType=daily-question&envId=2026-06-14
# Language: python3
# Date: 2026-06-14


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Use slow/fast pointers to find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half of the linked list in-place
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 'prev' is now the head of the reversed second half
        
        # 3. Iterate from both ends simultaneously to find the maximum twin sum
        max_twin_sum = 0
        left, right = head, prev
        while right:  # The second half will finish first or at the same time
            max_twin_sum = max(max_twin_sum, left.val + right.val)
            left = left.next
            right = right.next
            
        return max_twin_sum
