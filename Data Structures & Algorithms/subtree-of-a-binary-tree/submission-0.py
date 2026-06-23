# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Input: root and subRoot heads of binary trees
        # Output: if root has a subtree with the same structure as subRoot
        # Edges: 1 node
        # Constraints: [1,100] nodes; [-100,100] values

        # Test Cases
        # Happy Path
        # Input: root = [1,2,3,4,5], subRoot = [2,4,5]
        # Output: true
        # Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
        # Output: false
        # Input: root = [1], subRoot = [1]
        # Output: true
        #
        # Edges
        # Input: root = [1,2], subRoot = [2]
        # Output: true
        # Input: root = [3], subRoot = [1]
        # Output: false

        # DFS,BFS: HIGH
        # Recursion: HIGH
        # Iterative: HIGH

        # Strategy
        # Traverse each node in root
        # Check if the value matches the subroot
        # If it does, start checking the structure matches
        # If all nodes in subRoot match, return True
        # Else, continue traversing root and return False if none left

        # recursive each node
        # is it equal to subRoot?

        # If not, keep traversing
        # If is, check structure from there

        # If node is None, return (base case)
        # No need to handle if children are null yet

        def sameTree(root1, root2):
            if root1 is None or root2 is None:
                return root1 is None and root2 is None

            if root1.val != root2.val:
                return False
            
            return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)

        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        
        if sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
