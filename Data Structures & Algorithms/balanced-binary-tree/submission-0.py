# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Input: root of binary tree
        # Output: whether tree is height balanced
        # AKA whether left and right subtrees differ by <= 1 in height
        # edges: null root]
        # constraints:
        # [0,1000] inclusive nodes
        # [-1000,1000] inclusive values

        # Test cases:
        # Happy Path
        # Input: root = [1,2,3,null,null,4]
        # Output: true
        #
        # Input: root = [1,2,3,null,null,4,null,5]
        # Output: false
        #
        # Edge
        # Input: root = []
        # Output: true

        # Recursion: HIGH
        # DFS: HIGH
        # BFS: HIGH
        # Iterative: HIGH
        
        # Strategy
        # 0. Check root null
        # 1. Post order DFS in tree
        # 2. Base case: leaf -> (t, 1); null -> (t, 0)
        # 3. Bubble up: Check |h1-h2| <= 1 and subtrees are balanced
        # 4. At root, check height constraint and subtrees are balanced before returning final answer

        if root is None:
            return True

        def dfs(node):
            if node is None:
                return (True, 0)
            elif node.left is None and node.right is None:
                return (True, 1)

            balanced_1, height_1 = dfs(node.left)
            balanced_2, height_2 = dfs(node.right)
            return (
                balanced_1 and balanced_2 and abs(height_2 - height_1) <= 1, 
                max(height_1, height_2) + 1
            )
        
        balanced_1, height_1 = dfs(root.left)
        balanced_2, height_2 = dfs(root.right)

        return balanced_1 and balanced_2 and abs(height_2 - height_1) <= 1



