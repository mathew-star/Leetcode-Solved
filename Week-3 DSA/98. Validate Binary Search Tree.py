# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=[]
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right) 

        if root is None:
            return False
        inorder(root)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        
        return True