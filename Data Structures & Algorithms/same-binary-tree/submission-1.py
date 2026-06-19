# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative DFS

        # create dfs recursive helper method
        # - does post order traversal and checks values
        # - checks whether subtrees are equal
        # - return t/f whether subtrees and values are equal    
        st = [(p, q)]
        
        while st:
            node1, node2 = st.pop()

            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            
            st.append((node1.left, node2.left))
            st.append((node1.right, node2.right))
        return True