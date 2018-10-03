"""
Morris Traversal
Iterative, O(1) space, O(n) time
"""
def preorderTraversal(self, root):
 
    curr = root
    res = []
    while curr:
        if not curr.left:
            res.append(curr.val) 
            curr = curr.right
        else:
            pred = curr.left
            while pred.right and pred.right!= curr:
                pred = pred.right
            #if thereis a moriss thread, it means all preds are visited
            if pred.right:
                #res.append(curr.val) # put it here for in-order
                pred.right = None
                curr = curr.right
            #establish morris thread
            else: 
                res.append(curr.val) # pre-order
                pred.right = curr
                curr = curr.left
    return res
