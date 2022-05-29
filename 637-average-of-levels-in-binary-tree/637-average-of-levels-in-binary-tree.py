# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = [root]
        avg = []
        while q:
            count = len(q)
            _sum = 0
            for i in range(count):
                currNode = q.pop(0)
                _sum += currNode.val
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            avg.append(_sum/count)
        return avg
                
            