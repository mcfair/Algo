

#BFS method 1060ms
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #level order traversal
        bfs, ans = [root], 0
        
        #find all fully populated levels
        while all(bfs):
            ans += len(bfs)
            bfs = [child for x in bfs for child in (x.left, x.right)]
        
        #handle last layer    
        if any(bfs):
            N = len(bfs) - bfs.count(None)
            for i in range(N):
                if not bfs[i]:
                    return ans
            return ans + N           
        else:
            return ans
