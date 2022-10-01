# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        res = []
        p = root
        while stack or p:
            if not p: 
                p = stack.pop()
                res.append(p.val)
                p = p.right
                continue
            stack.append(p)
            p = p.left
                
        return res[k - 1]
        
        
        
        
        # O(n) time and space
        res = []
        def inorder(p):
            if not p: return
            inorder(p.left)
            res.append(p.val)
            inorder(p.right)
        inorder(root)
        return res[k - 1]