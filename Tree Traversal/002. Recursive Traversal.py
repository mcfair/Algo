def preorderTraversal(root):
    if not root: return []
    res = []
    res.append(root.val)
    res.extend(self.preorderTraversal(root.left))
    res.extend(self.preorderTraversal(root.right))
    return res
  
def inorderTraversal(root):
    if not root: return []
    res = []
    res.extend(self.inorderTraversal(root.left))
    res.append(root.val)
    res.extend(self.inorderTraversal(root.right))
    return res 

def postorderTraversal(root):
    if not root: return []
    res = []
    res.extend(self.postorderTraversal(root.left))
    res.extend(self.postorderTraversal(root.right))
    res.append(root.val)
    return res
