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
                               
                
  
def postorderTraversal(self, root):
    def reverseOrder(l, r):
        while l < r:
            result[l],result[r] = result[r],result[l]
            l, r = l+1, r-1

    result=[]
    cur= TreeNode(None) #dummynode
    cur.left = root

    while cur!=None: 
        if cur.left==None:
            cur=cur.right
        else:
            pre=cur.left
            while pre.right!=None and pre.right!=cur:
                pre=pre.right
            if pre.right==None:
                pre.right=cur
                cur=cur.left
            else:
                pre=cur.left
                count=1
                while pre.right!=None and pre.right!=cur:
                    result.append(pre.val)
                    pre=pre.right
                    count+=1
                result.append(pre.val)
                pre.right=None
                reverseOrder(len(result)-count,len(result)-1)
                cur=cur.right
    return result
