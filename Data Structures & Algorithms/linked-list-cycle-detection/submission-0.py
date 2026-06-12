# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Input: head of linked list
        # Output: true if cycle, false if not
        # Edges: null head, node cycles to itself
        
        # Test cases:
        # Happy Path
        # head = [1,2,3,4], index = 1 (cycle at 2)
        # head = [1,2,3,4], index = -1 (no cycle)
        
        # Edges
        # head = [], index = -1 (empty)
        # head = [1], index = 0 (cycles in place)
        # head = [1,2,...,1000], index = 0 (max size cycles to start)

        # Questions
        # Can multiple nodes contain the same value?

        # Linked-list: HIGH
        # Recursion: MED
        # Two-pointer (fast and slow): HIGH
        
        # Strategy
        # Fast and slow pointer.
        # Slow iterates to node.next each round
        # Fast iterates to node.next.next each round
        # Not just values are the same, object references?
        # If there's a cycle, slow and fast will meet before slow | fast == None

        # head = [1,2,3,4], index = 1
        # s = 1->2->3->4
        # f = 1->3->2->4
        # return true

        # head = [1]
        # s = 1->1
        # f = 1->1
        # return true

        # head = []
        # return false

        # 1. Check if head is null
        # 2. Initialize and slow/fast pointers
        # 3. Loop until pointers are same object or either (likely fast) is null
        # 4. If either is null return false, otherwise return true

        if not head:
            return False
        
        slow = head
        fast = head.next

        while slow and fast and slow != fast:
            slow = slow.next
            fast = fast.next
            if fast: # Can't do .next on a None
                fast = fast.next

        # both are equal node
        # one or both are null
        return slow == fast and slow != None

        # O(n) time
        # O(1) space
