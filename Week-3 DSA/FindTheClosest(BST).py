class Node:
    def __init__(self,val):
        self.val=val
        self.left=self.right=None
def  insert(root,value):
    if root is None:
        return  Node(value)
    else:
        if value<root.val:
            root.left=insert(root.left,value)
        else:
            root.right=insert(root.right,value)
    return root

def inorder(node):
    if node:
        inorder(node.left)
        print(node.val,end=" ")
        inorder(node.right)
        
def findClosest(root,target):
    close=root.val
    while root:
        if abs(root.val-target)< abs(close-target):
            close=root.val
        if target<root.val:
            root=root.left
        elif target> root.val:
            root=root.right
        else:
            return root.val
    return close
      
root=None
root=insert(root,50)
insert(root,30)
insert(root,10)
insert(root,60)

inorder(root)
print(" ")
print(findClosest(root,9))