# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive solution
        # "Reverse the rest then fix the pointer to the current"

        # If list is empty return null
        # Call function on head.next to reverse list
        # After recursion returns, make head.next.next = head
        # Set head.next = null to avoid cycles
        # Return head returned by deepest recursive call

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead