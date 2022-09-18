# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative Approach
        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
        
        # Recursive Approach
        # res = []
        # def dfs(root):
        #     if not root: return
        #     if root.left: dfs(root.left)
        #     res.append(root.val)
        #     if root.right: dfs(root.right)
        # dfs(root)
        # return res
            