# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS
        # Keep track of depth in stack

        st = [(root, 1)]
        max_depth = 0
        while len(st) > 0:
            node, depth = st.pop()

            if node:
                max_depth = max(max_depth, depth)
                st.append((node.left, depth+1))
                st.append((node.right, depth+1))
            
        return max_depth
