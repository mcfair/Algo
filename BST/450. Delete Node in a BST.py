class Solution(object):
    def deleteNode(self, root, key):
        if root is None:
            return None
        
        if root.val == key:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
            # if the node has both left and right children,  
            # we replace its value with the minmimum value in the right subtree 
            # then we delete that min-val node in the right subtree
                root.val = self.smallest(root.right)
                root.right = self.deleteNode(root.right, root.val)
            
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
            
        return root
    
    def smallest(self, node):
        while node.left is not None:
            node = node.left
        return node.val
