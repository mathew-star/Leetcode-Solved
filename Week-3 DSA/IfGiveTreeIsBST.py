class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
res=[]
def inorder(root):
    if root:
        inorder(root.left)
        res.append(root.data)
        print(root.data, end=" ")
        inorder(root.right) 

def is_bst(root):
    if root is None:
        return False
    inorder(root)
    for i in range(len(res)):
        swaped=False
        for j in range(0,len(res)-i-1):
            if  res[j] < res[j+1]:
                pass
                swaped=True
        if swaped==False:
            break
    return True if swaped==False else False
    
                
    

if __name__ == "__main__":
    # Constructing a BST
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)

    # Validating if it's a BST
    if is_bst(root):
        print("The tree is a Binary Search Tree.")
    else:
        print("The tree is not a Binary Search Tree.")
