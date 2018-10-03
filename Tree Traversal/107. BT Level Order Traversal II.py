class Solution(object):
    def levelOrderBottom(self, root):
        
        if not root: return []
        bfs, res = [root], []
        while bfs:
            res.append([node.val for node in bfs])
            bfs = [kid for node in bfs for kid in (node.left,node.right) if kid]
        return res[::-1]
        
