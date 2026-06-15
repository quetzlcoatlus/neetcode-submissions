# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # input: root of binary tree
        # output: root of inverted binary tree
        # edge: root is null, uneven tree, only root

        # Test cases (level-order)
        # Happy Path
        # input: root = [1,2,3,4,5,6,7]
        # output: [1,3,2,7,6,5,4]
        #
        # input: root = [3,2,1]
        # ouput: [3,1,2]
        #
        # Edge Case
        # input: root = []
        # output: []
        #
        # input: root = [1]
        # output: [1]
        #
        # input: root = [1,2,3,4,5]
        # output: [1,3,2,5,4]

        # Binary tree: HIGH
        # Recursion: HIGH
        # Iteration: HIGH

        # Strategy
        # Recursive solution
        # Given a node, swap its left and right pointers
        # Before this, I would recursively check the node's left and right
        # Base Case: If a node is a leaf or none, nothing to swap so we return
        # So at a node, ask children to fix themselves and swap my two pointers
        # Recusion handles the subtrees, then I swap pointers

        # 1. Check base case
        # 2. Ask left and right to fix themselves
        # 3. Fix current node by swapping left and right pointers

        if root is None or root.left is None and root.right is None:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root

        # Validate
        # [1,2,3]
        # root = 1, invertTree(2)
        # root = 2, left and right are none so return
        # root = 3, left and right are none so return
        # root = 1, root.left = 3, root.right = 2
        # return [1,3,2]
        #
        # []
        # return []
        # 
        # [1]
        # is leaf
        # return [1]

        
