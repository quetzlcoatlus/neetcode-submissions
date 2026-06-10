# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Given a head of a linked list
        # Output the head of reversed list
        # Edge cases for linked lists with loops or length 0

        # Test cases
        # - [0, 1, 2, 3]    Happy Path
        # - []              Edge Case (empty)
        # - [1, 2, 1]       Edge Case (palindrome)
        # - [1, 2, 1, 2]    Edge Case (repeating values)

        # Constraints
        # Length [0, 1000]
        # Values [-1000, 1000] inclusive

        # Questions
        # Loops possible?
        # Is this doable in one pass?
        # Is this doable with constant memory?

        # Linked list: HIGH
        
        # Plan:
        # Reversing the list means reversing the way that each node points
        # Example:
        # 0->1->2->3
        # 3->2->1->0
        # One at a time
        # while head:
        #   prev = null
        #   temp = head
        #   head = head.next
        #   temp.next = prev
        #   prev = temp
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev

        # O(n) time
        # O(1) space
        
