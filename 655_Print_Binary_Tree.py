class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        
        My naive solution, 28ms beat 100%,  O(m*n)
        (1)Use dfs to find tree height 'm', then calculate width 'n' and center 'c'
        (1)Use bfs to do level order traversal
        (2)Replace null node with TreeNode("") in each level/row.
        (3)Calculate the position of the node, which is its parent position +/- 2^(m-i-2)
       
        """
        
        m = self.findDepth(root) #height of the matrix
        n = sum(2**i for i in range(m)) #width of the matrix
        c = n/2  #center of each row, n must be odd,index starts from 0
      
        bfs, tmp, ans, pos = [root] , ['']*n, [], [c]
         
        for i in range(m):
          
            for j,x in enumerate(bfs):
                tmp[pos[j]] = str(x.val)
                
            ans.append(tmp)
            tmp = ['']*n
            
            bfs = [ child if child else TreeNode("")
                    for x in bfs 
                        for child in (x.left,x.right )]
              
            newpos =[]
            for p in pos:
                newpos.append(p - 2**(m-i-2))
                newpos.append(p + 2**(m-i-2))
            pos = newpos
        return ans
            
            
          
    def findDepth(self,root):
        if not root: return 0
        return 1 + max(self.findDepth(root.left), self.findDepth(root.right))
