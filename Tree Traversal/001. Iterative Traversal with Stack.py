"""
Summarization of three different kinds of traversal.
we only need to change the order of tuples in one line as we've done this in the recursive solution 
Just put (0, p[1]) in different position!
"""

#post-order traversal
def postorderTraversal(self, root):
    res, stack = [], [(1, root)]
    while stack:
        p = stack.pop()
        if not p[1]: continue
        if p[0] != 0:
            stack.extend([(0, p[1]), (1, p[1].right), (1, p[1].left)])  
        else:
            res.append(p[1].val)
    return res
  
#in-order traversal
def inorderTraversal(self, root):
    res, stack = [], [(1, root)]
    while stack:
        p = stack.pop()
        if not p[1]: continue
        if p[0] != 0:
            stack.extend([(1, p[1].right), (0, p[1]), (1, p[1].left)])  
        else:
            res.append(p[1].val)
    return res

#pre-order traversal
def preorderTraversal(self, root):
    res, stack = [], [(1, root)]
    while stack:
        p = stack.pop()
        if not p[1]: continue
        if p[0] != 0:
            stack.extend([(1, p[1].right), (1, p[1].left), (0, p[1])]) 
        else:
            res.append(p[1].val)
    return res
