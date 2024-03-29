# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append('x')
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res_as_strings = [str(item) for item in res]
        return " ".join(res_as_strings)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(nodes):
                val = next(nodes)
                if val == 'x': return
                cur = TreeNode(int(val))
                cur.left = dfs(nodes)
                cur.right = dfs(nodes)
                return cur

        return dfs(iter(data.split()))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))