# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def treeheight(node):
            if node is None:
                return 0
            l=treeheight(node.left)
            r=treeheight(node.right)
            if l is -1 or r is -1:
                return -1
            if abs(l-r)>1:
                return -1
            return max(l,r)+1

        return treeheight(root) != -1
        