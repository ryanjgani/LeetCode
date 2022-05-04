# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def inorder(p):
            if p:
                inorder(p.left)
                arr.append(p.val)
                inorder(p.right)
        inorder(root)
        d = {}
        for i, n in enumerate(arr):
            if k - n in d:
                return True
            d[n]=i
        return False
            
        