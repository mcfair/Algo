"""
direct recursion
"""
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

"""
recursive generator
"""
def preorderGen(root):
    if root:
        yield root
        for x in preorderGen(root.left): yield x
        for x in preorderGen(root.right): yield x
        
        
def inorderGen(root):
    if root:
        for x in inorderGen(root.left): yield x
        yield root
        for x in inorderGen(root.right): yield x
        
def postorderGen(root):
    if root:
        for x in postorderGen(root.left): yield x
        for x in postorderGen(root.right): yield x
        yield root
        
#driver function example
def postorderTraversal(root):
    return [x.val for x in postorderGen(root)] 
