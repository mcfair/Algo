class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        bfs = [root]
        res = []
        zigzag = 0
        while bfs:
            row = [node.val for node in bfs]
            if zigzag:
                res.append(row[::-1])
            else:
                res.append(row)
            zigzag ^=1
            
            bfs = [node for x in bfs for node in (x.left, x.right) if node]        
            
        return res
            
