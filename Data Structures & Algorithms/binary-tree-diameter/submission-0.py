# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # input: root of binary tree
        # output: int diameter of binary tree
        # edges: null root

        # Test Cases
        # Happy path
        # input: root = [1,null,2,3,4,5]
        # output: 3
        #
        # Small case
        # input: root = [1,2,3]
        # output: 2
        # 
        # Edges
        # input: root = []
        # output: 0

        # Questions
        # Diameter is length of longest path between any two nodes

        # DFS: HIGH
        # BFS: HIGH
        # Q/Stack: HIGH
        # Recursion: HIGH

        # Strategy
        # Assume we can get height of subtrees, what happens at single node?
        # root = [1,2,3]
        # diameter is sum of the result of subtrees, keep track of max globally
        # we return the longest distance so max(subtrees)
        # diameterOfBinaryTree(1)->sum of subtrees = d = 2, h = 1
        # | diameterOfBinaryTree(2)->is leaf d=0->1+subtrees = 1
        # | diameterOfBinaryTree(3)->is leaf d=0->1+subtrees = 1
        #
        # root = []
        # diameterOfBinaryTree(null)->0
        #
        # root = [1,null,2,3,4,5]
        # d = 0->1->3
        # d(1) d = ret sum(subtrees) = 3; h = max(subtrees) + 1 = 4
        # d(2) d = sum(subtrees) = 3; ret h = max(subtrees) + 1 = 3
        # d(3) d = sum(subtrees) = 1; ret h = max(subtrees) + 1 = 2
        # d(5) d = sum(subtrees) = 0; ret h = max(subtrees) + 1 = 1
        # d(4) d = sum(subtrees) = 0; ret h = max(subtrees) + 1 = 1
        #
        # root = [1,2,3,4,5,6,7]
        # d = 0->2->4
        # 1->2->4..2->5..2..1->3->6..3->7..3..1
        # d(1) -> d = sum(subtrees) = 4; h = max(subtrees) + 1 = 3
        # d(2) -> d = sum(subtrees) = 2; h = max(subtrees) + 1 = 2
        # d(4) -> d = sum(subtrees) = 0; h = max(subtrees) + 1 = 1
        # d(5) -> d = sum(subtrees) = 0; h = max(subtrees) + 1 = 1
        # d(3) -> d = sum(subtrees) = 2; h = max(subtrees) + 1 = 2
        # d(6) -> d = sum(subtrees) = 0; h = max(subtrees) + 1 = 1
        # d(7) -> d = sum(subtrees) = 0; h = max(subtrees) + 1 = 1

        # establish global variable
        # helper function that calculates height of bt
        # calculate subtrees

        max_diameter = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            nonlocal max_diameter # or make member variable
            max_diameter = max(max_diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return max_diameter

        # Time: O(n) checking each node once
        # Space: O(log(n)) if balanced
        # Space: O(n) if unbalanced
        
