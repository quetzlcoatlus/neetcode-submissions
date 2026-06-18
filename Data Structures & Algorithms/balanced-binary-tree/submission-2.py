# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Iterative DFS strategy

        # Strategy
        # 0. Check root null
        # 1. Post order DFS in tree
        # 2. Base case: leaf -> (t, 1); null -> (t, 0)
        # 3. Bubble up: Check |h1-h2| <= 1 and subtrees are balanced
        # 4. At root, check height constraint and subtrees are balanced before returning final answer
        if root is None:
            return True
        
        st = [root]
        depths = {}

        while st:
            node = st[-1]
            if node.left and node.left not in depths:
                st.append(node.left)
            elif node.right and node.right not in depths:
                st.append(node.right)
            else:
                node = st.pop()
                left = depths.get(node.left, 0)
                right = depths.get(node.right, 0)

                if abs(left - right) > 1:
                    return False
                
                depths[node] = 1 + max(left, right)
        return True           
            
        # def dfs(node):
        #     if node is None:
        #         return (True, 0)
        #     elif node.left is None and node.right is None:
        #         return (True, 1)

        #     balanced_1, height_1 = dfs(node.left)
        #     balanced_2, height_2 = dfs(node.right)
        #     return (
        #         balanced_1 and balanced_2 and abs(height_2 - height_1) <= 1, 
        #         max(height_1, height_2) + 1
        #     )
        # return dfs(root)[0]