class Node(object):
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 
class BST(object):
    def __init__(self, root=None):
        self.root = root
        
    def insert(self, node):
        if not self.root:
            self.root = node
        else:
            if self.root.val < node.val:
                if self.root.right is None:
                    self.root.right = node
                else:
                    self.insert(self.root.right, node)
            else:
                if self.root.left is None:
                    self.root.left = node
                else:
                    self.insert(self.root.left, node)

     def search(self, val):
        if not self.root:
            return None
        if val == self.root.val:
            return root
        elif val < self.root.val:
            return self.search(self.root.left, val)
        elif val > self.root.val:
            return self.search(self.root.right, val)
