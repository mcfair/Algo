#O(n) time, O(n) space

def inorderIter(root):
    if root:
        for node in inorderIter(root.left): 
            yield node
        yield root        
        for node in inorderIter(root.right): 
            yield node
    
class Solution(object):
    def recoverTree(self, root):
        prev, first, second = None, None, None
        for node in inorderIter(root):
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                    second = node
                else:
                    second = node
            prev= node
        
        #swap    
        first.val, second.val = second.val, first.val
 
#O(n) time, O(1) space, Morris Traversal
#https://www.jianshu.com/p/d2059062efac
def morris_in_order(root):
    curr = root
    while curr:
        if not curr.left:
            yield curr 
            curr = curr.right
        else:
            # find current node's predecessor = rightmost node of the left subtree
            pred = curr.left 
            while pred.right and pred.right!= curr:
                pred = pred.right

            #morris threading: use predecessor's right pointer to connect with current node
            if not pred.right:
                pred.right = curr
                curr = curr.left
            #if there is a connection, visit the current node then delete the threading
            else:
                yield curr 
                pred.right = None
                curr = curr.right
  
#same driver function as line 11           
class Solution(object):
    def recoverTree(self, root):       
        prev, first, second = None, None, None
        for curr in morris_in_order(root):
            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                    second = curr
                else:
                    second = curr
            prev = curr
         
        first.val, second.val = second.val, first.val
         
