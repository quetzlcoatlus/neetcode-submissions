# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # input: root of two binary trees p and q
        # output: whether same structure and node values
        # edges: either null
        # constraint: [0,100] nodes; [-100,100] values

        # test cases
        # happy path
        # p = [1,2,3], q = [1,2,3]
        # true
        # p = [4,7], q = [4,null,7]
        # false
        # p = [1,2,3], q = [1,3,2]
        # false
        # 
        # edges
        # p = null, q = null
        # true
        # p = null, q = [1]
        # false

        # DFS/BFS: HIGH
        # Recursion: HIGH
        # Iterative: HIGH
        
        # strategy
        # pick a consistent traversal method (e.g. post order)
        # check values for equality
        # if they're equal, continue otherwise break

        # recursion
        # base case: leaf or null
        # bubble up whether we're still equal, individual step check equality

        # 1. p = [1,2,3], q = [1,2,3]
        # dfs(p1, q1) equal
        # - dfs(p2, q2) equal
        # - dfs(p3, q3) equal
        # true
        # 2. p = [1,2,3], q = [1,3,2]
        # dfs(p1, q1) not equal
        # - dfs(p2, q3) not equal
        # - dfs(p3, q2) not equal
        # false
        # 3. p = [], q = [1]
        # dfs(null, q1) not equal
        # false
        # 4. p = [], q = []
        # dfs(null, null) equal
        # true

        # create dfs recursive helper method
        # - does post order traversal and checks values
        # - checks whether subtrees are equal
        # - return t/f whether subtrees and values are equal
        
        def dfs(node1, node2):
            if node1 is None or node2 is None:
                return node1 is None and node2 is None
            
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right and node1.val == node2.val
        return dfs(p, q)

            


