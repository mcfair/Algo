# New skills get
# In BFS level order traversal, construct a tuple of (node, other_info)

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        cols = collections.defaultdict(list)
        

        bfs = [(0, root)]  #root is col 0, and left will be negative columns, and right is positive
        
        while bfs:
            for i, node in bfs:
                cols[i].append(node.val)
            bfs = [kid for i, x in bfs 
                        for kid in ((i-1,x.left), (i+1, x.right) ) if kid[1]]
        
        return [cols[i] for i in sorted(cols)]
        
