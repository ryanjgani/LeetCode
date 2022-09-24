# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root: return [0, 0]
            
            leftR, leftW = dfs(root.left)
            rightR, rightW = dfs(root.right)
            res = [root.val + leftW + rightW , max(leftR, leftW) + max(rightR, rightW)]
            return res
        res = dfs(root)
        return max(res)
                
            
            
            