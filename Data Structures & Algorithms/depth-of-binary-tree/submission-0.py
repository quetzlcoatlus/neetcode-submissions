# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Input: root of binary tree
        # Output: integer value of tree depth
        # Edges: unbalanced tree, null root

        # Test Cases
        # Happy Path
        # input: root = [1,2,3,null,null,4] (level-order)
        # output: 3
        #
        # Edges
        # input: root = []
        # output: 0
        #
        # input: root = [1,null,2,null,null,null,3,null,null,null,null,null,null,null,4]
        # output: 4

        # Questions:
        # nodes = [0,100] inclusive
        # node.val = [-100,100] inclusive

        # Strategy
        # DFS: HIGH
        # BFS: HIGH
        # Stack/Queue: HIGH
        # Recursion: HIGH

        # Recursive solution first even though I know iterative is possible
        # Max depth means the deepest level
        # Assume subtrees we can find the max depth
        # For [1,2,3,null,null,4] at 1, assume subtrees return a depth
        # At 1, all we need to do is add the current depth (1) to the depth of the deepest subtree
        # 5 states for a node: null, leaf, has left, has right, has both

        # Ask children for their depths
        # Take the bigger one
        # Add 1 for myself

        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


