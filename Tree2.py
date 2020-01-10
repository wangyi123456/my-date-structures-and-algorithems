class TreeNode ():
    def __init__ (self,val):
        self.val = val
        self.left , self.right = None , None
class Tree ():
    def __init__ (self,root = None):
        self.root = root
    def insert (self,num):
        node = TreeNode(num)
        if self.root == None:
            self.root = node
        else:
            temp = self.root
            while temp:
                if num < temp.val:
                    if temp.left == None:
                        temp.left = node
                        return
                    else:
                        temp = temp.left                  
                if num > temp.val:
                    if temp.right == None:
                        temp.right = node
                        return
                    else:
                        temp = temp.right
def get_height (root):
        if root == None:
            return 0
        else:
            L_height = get_height(root.left)
            R_height = get_height(root.right)
            h = L_height
            if R_height >L_height:
                h = R_height
            return h+1
def get_max (root):
    if root == None:       
        return -1
    else:
        m = root.val
        lm = get_max(root.left)
        rm = get_max(root.right)
        if lm > m:
            m = lm
        if rm > m:
            m = rm
        return m
    
            
            
def preorder (root):
    if root:
        print (root.val)
        preorder (root.left)
        preorder (root.right)
        
test = [6,3,8,2,5,1,7]
tree = Tree()
for item in test:
    tree.insert(item)
print (get_height(tree.root))
print (get_max(tree.root))