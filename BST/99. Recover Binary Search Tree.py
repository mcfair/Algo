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
                    break
            prev= node
        
        #swap    
        first.val, second.val = second.val, first.val
 
#O(n) time, O(1) space, Morris Traversal
#https://www.jianshu.com/p/d2059062efac
