```
def isSameTree(p, q):
    if not p and not q: return True
    if not p or not q: return False
    if p.val != q.val: return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def isSubtree(s, t):
    if not s: return False
    #like preorder  
    return isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
```
