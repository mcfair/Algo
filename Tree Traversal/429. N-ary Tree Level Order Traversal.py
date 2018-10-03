
class Solution(object):
    def levelOrder(self, root):
 
        if not root: return []
        stack = [root]
        res = []
        while stack:
            res.append([node.val for node in stack])
            next_row = []
            for node in stack:
                next_row.extend(node.children)
            stack = next_row
        return res
        
