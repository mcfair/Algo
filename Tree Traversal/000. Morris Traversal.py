def morris_in_order(root):
    curr = root
    while curr:
        if not curr.left:
            yield curr.val
            curr = curr.right
        else:
            # find current node's predecessor = rightmost node of the left subtree
            pred = curr.left 
            while pred.right and pred.right!= curr:
                pred = pred.right
             
            #morris threading: 
            #if not connected yet: use predecessor's right pointer to connect with current node
            if not pred.right:
                pred.right = curr
                curr = curr.left
            #if there is a connection, visit the current node then delete the threading
            else:
                yield curr.val
                pred.right = None
                curr = curr.right
                
                
                
def morris_pre_order(root):
    curr = root
    while curr:
        if not curr.left:
            yield curr.val
            curr = curr.right
        else:
            # find current node's predecessor = rightmost node of the left subtree
            pred = curr.left 
            while pred.right and pred.right!= curr:
                pred = pred.right
             
            #morris threading: use predecessor's right pointer to connect with current node
            if not pred.right:
                yield curr.val
                pred.right = curr
                curr = curr.left
            #if there is a connection, visit the current node then delete the threading
            else:
                pred.right = None
                curr = curr.right
                               
                
  
