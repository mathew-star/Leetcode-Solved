# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def inorder(root):
            if root is None:
                return [None]
            return [root.val] + inorder(root.left) + inorder(root.right)
        print(inorder(p))
        print(inorder(q))
        
        return inorder(p) == inorder(q)