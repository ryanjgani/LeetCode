# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         if not root: return []
#         res = []
#         queue = [root]
#         while queue:
#             length = len(queue)
#             for i in range(length):
#                 node = queue.pop(0)
#                 if i == length - 1: res.append(node.val)
#                 if node.left: queue.append(node.left)
#                 if node.right: queue.append(node.right)
#         return res
        res = []
    
        def dfs(node, depth):
            nonlocal res
            if not node: return
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res