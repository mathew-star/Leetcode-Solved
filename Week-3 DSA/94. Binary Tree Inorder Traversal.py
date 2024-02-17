# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return []

        def Inorder(root):

            if root:
                Inorder(root.left)
                res.append(root.val)
                Inorder(root.right)
                
        Inorder(root)
        return res