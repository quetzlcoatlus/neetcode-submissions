# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative DFS approach
        # Can use an explicit stack instead
        if not root:
            return None

        st = [root]
        while st:
            curr = st.pop()
            curr.left, curr.right = curr.right, curr.left
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
        return root

        # Also
        # O(N) time
        # O(N) space, but no risk of stack overflow in program memory!
