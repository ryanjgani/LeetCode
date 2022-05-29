# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, count):
            if not node:
                return
            
            # leaf
            if not node.left and not node.right:
                if count + node.val == targetSum:
                    return True
                return
            count += node.val
            return dfs(node.left, count) or dfs(node.right, count)

        if dfs(root, 0):
            return True
        else:
            return False