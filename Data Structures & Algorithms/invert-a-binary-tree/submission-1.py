# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS approach
        if not root:
            return None

        q = deque([root])
        while q:
            curr = q.popleft()
            # for list this is O(n) so using a queue structure is better
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root

        # Same as dfs recursive approach
        # O(N) time
        # O(N) space


