# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        stack = []
        
        # Iterative
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.inorder.append(root.val)
            root = root.right
        
        
        # Recursive
        # def dfs(root):
        #     if not root: return
        #     if root.left: dfs(root.left)
        #     self.inorder.append(root.val)
        #     if root.right: dfs(root.right)
        # dfs(root)   
        

    def next(self) -> int:
        return self.inorder.pop(0)

    def hasNext(self) -> bool:
        return len(self.inorder) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()