# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def inorder(node):
            if not node:
                return
            if node.left: inorder(node.left)
            arr.append(node.val)
            if node.right: inorder(node.right)
                
        arr = []
        inorder(root)
        print(arr)
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True
            
        
        