# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Input: heads of two sorted linked lists
        # Output: head of one merge sorted linked list
        # Edges: >= 1 list length == 0

        # Test cases:
        # Happy Path
        # l1 = [1,2,4], l2 = [1,3,5]
        # Expected: [1,1,2,3,4,5]
        # 
        # Edges
        # l1 = [], l2 = [1,2]
        # Expected: [1,2]
        #
        # l1 = [], l2 = []
        # Expected: []
        
        # Merge Sort: HIGH
        # Recursion: MED
        # Iterative: MED

        # Strategy
        # Iterative keeping first node reference to return
        # Edges dealt with by returning head of non-null list or null if both are
        # l1 = [1,2,4], l2 = [1,3,5]
        # h = NULL->1
        # p = NULL->1->1->2->3->4->5
        # Both are 1, so save l1 in h
        # Save previous to p = l1 so we can set next
        # Default to iterating l1. l1 = l1.next
        # l1 is 2 and l2 is 1, so we set
        # p.next = l2, p = l2, l2 = l2.next
        # l1 = 2 and l2 = 3 so, p.next = l1
        # p = l1 and l1 = l1.next
        # l1 = 4 and l2 = 3, so p.next = l2
        # p = l2, l2 = l2.next
        # l1 = 4, l2 = 5, so p.next = l1
        # p = l1, l1 = l1.next
        # l1 is Null and l2 is 5,
        # p = l2, break since we append the rest of l2 automatically
        # return h

        # 1. Check heads if they're null. If at least one is, then no work to do
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        # 2. Set initial pointer variables to null
        dummy = prev = ListNode()

        # 3. Compare the node values and iterate the head of the lower value. Ties default to l1.
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                # 4. Set pointer variables and iterate head
                prev.next = list1
                list1 = list1.next
            else:
                # 4. Set pointer variables and iterate head
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        # 5. When either of the heads become null, set prev.next to the non-null and break
        prev.next = list1 or list2

        return dummy.next

        # O(n) time
        # O(1) space

