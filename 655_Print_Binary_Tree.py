class Solution(object):
    #Two methoeds: recursive(dfs) & iterative(bfs)
    
    def printTree_recusive(self, root):
        """
        Calculate the position of each node from its parent position p +/- 2^(m-row-2)
        Starting from root, where row=0, pos=c. Then recursively find all childrens.
        """
        m = self.findDepth(root) #height of the matrix
        n = 2**m -1
        c = n/2  
       
        res = [[""]* n for _ in range(m)]
        def dfs(node, row, pos):
            if not node: return
            res[row][pos]=str(node.val)
            dfs(node.left, row+1, pos - 2**(m-row-2))
            dfs(node.right, row+1, pos + 2**(m-row-2))
            
        dfs(root, row=0, pos=c)
        return res
            
    def printTree_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        
        My iterative solution, 28ms beat 100%,  O(m*n)
        (1)Use dfs to find tree height 'm', then calculate width 'n' and center 'c'
        (1)Use bfs to do level order traversal
        (2)Replace null node with TreeNode("") in each level/row.
        (3)Calculate the position of each node, which is its parent position +/- 2^(m-i-2)
       
        Additional math, given a Binary Tree of height H:
            The maximum total number of nodes is = 2^H - 1
            Number of nodes at each level, L (0-indexed) = 2^L
        """
        
        m = self.findDepth(root) #height of the matrix
        n = 2**m -1
        #n = sum(2**i for i in range(m)) #width of the matrix  n = 2^m -1
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
    

        
