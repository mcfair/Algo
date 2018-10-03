class Solution(object):
    def levelOrder(self, root):
 
        if not root: return []
        bfs, res =[root], []
        
        while bfs:
            res.append([x.val for x in bfs])
            bfs = [child for x in bfs 
                            for child in (x.left, x.right) if child]
        return res
