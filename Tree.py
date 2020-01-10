class TreeNode ():
    def __init__ (self,val):
        self.val = val
        self.left , self.right = None , None

"""class Tree:
    def __init__ (self,root):
        self.root = None
   """
def preorder (root):
    if root:
        print (root.val)
        preorder (root.left)
        preorder (root.right)

a = TreeNode (1)
b = TreeNode (2)
c = TreeNode (3)
d = TreeNode (4)
e = TreeNode (5)
f = TreeNode (6)
g = TreeNode (7)
h = TreeNode (8)
e.left , e.right = c , g
c.left , c.right = b , d
b.left  = a 
g.left , g.right = f , h
root = e
preorder (root)