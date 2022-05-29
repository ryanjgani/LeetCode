# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def maxDepth(node):
            if not node:
                return 0
            return 1 + max(maxDepth(node.left), maxDepth(node.right))
        
        maxDiameter = 0
        def diameter(node):
            nonlocal maxDiameter
            if not node:
                return 0
            maxLeft = diameter(node.left)
            maxRight = diameter(node.right)
            maxDiameter = max(maxDiameter, maxLeft + maxRight)
            return max(maxLeft, maxRight) + 1
        diameter(root)
        return maxDiameter
        
        
        
    
    
    
        
        
            