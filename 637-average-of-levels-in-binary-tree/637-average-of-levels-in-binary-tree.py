# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = [root]
        while queue:
            n = len(queue)
            count = 0
            for i in range(n):
                top = queue.pop(0)
                count += top.val
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)
            res.append(count / n)
        return res