# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left, right = float('-inf'), float('inf')
        
        def dfs(p, l, r):
            if not p: return True
            if (p.right and p.val >= p.right.val) or (p.left and p.val <= p.left.val) or p.val >= r or p.val <= l:
                return False
            return dfs(p.left, l, p.val) and dfs(p.right, p.val, r)
        
        return dfs(root, left, right)
            