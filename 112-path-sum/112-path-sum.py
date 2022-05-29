# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        print("****")
        if not root:
            return False
        def dfs(node, count):
            # leaf
            if not node:
                return
            print(node.val)
            if not node.left and not node.right:
                if count + node.val == targetSum:
                    return True
                return
            count += node.val
            return dfs(node.left, count) or dfs(node.right, count)
        
        
        
        
        #     if not node.left or not node.right:
        #         print(count + node.val, targetSum, count == targetSum)
        #         if count + node.val == targetSum:
        #             return True
        #         return
        #     count += node.val
        #     return dfs(node.left, count) or dfs(node.right, count)
        #     count -= node.val
        if dfs(root, 0):
            return True
        else:
            return False