class Node(object):
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 
class BST(object):
    def __init__(self, root=None):
        self.root = root
        
    def insert(self, node, root=self.root):
        if not root:
            root = node
        else:
            if root.val < node.val:
                self.insert(node, root.right)
            else:
                self.insert(node, root.left)

     def search(self, val, root=self.root):
        if not root:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            return self.search(val, root.left)
        elif val > root.val:
            return self.search(val, root.right)
