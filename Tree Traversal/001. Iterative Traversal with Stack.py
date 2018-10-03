"""
Summarization of three different kinds of traversal.
In this template, we only need to change the order of tuples in one line as we've done this in the recursive solution. 
Just put (1, node) in different position, where 1 is the "visited" flag
"""

#post-order traversal
def postorderTraversal(self, root):
    res, stack = [], [(0, root)]
    while stack:
        seen, node = stack.pop()
        if not node:
            continue
        if not seen:
            stack.extend([(1, node), (0, node.right), (0, node.left)])
        else:
            res.append(node.val)
    return res


#in-order traversal
def inorderTraversal(self, root):
    res, stack = [], [(0, root)]
    while stack:
        seen, node = stack.pop()
        if not node:
            continue
        if not seen:
            stack.extend([(0, node.right), (1, node), (0, node.left)])
        else:
            res.append(node.val)
    return res 

#pre-order traversal
def preorderTraversal(self, root):
    res, stack = [], [(0, root)]
    while stack:
        seen, node = stack.pop()
        if not node:
            continue
        if not seen:
            stack.extend([(0, node.right), (0, node.left), (1, node)])
        else:
            res.append(node.val)
    return res 
