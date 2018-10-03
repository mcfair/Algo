# 102. Binary Tree Level Order Traversal
def levelOrder(self, root):
    if not root: return []
    bfs, res =[root], []

    while bfs:
        res.append([x.val for x in bfs])
        bfs = [child for x in bfs for child in (x.left, x.right) if child]
    return res

# 107. Binary Tree Level Order Traversal II
def levelOrderBottom(self, root):
    if not root: return []
    bfs, res = [root], []
    while bfs:
        res.append([node.val for node in bfs])
        bfs = [kid for node in bfs for kid in (node.left,node.right) if kid]
    return res[::-1]  #only this line is dffierent from LC102
    
# 637. Average of Levels in Binary Tree
def averageOfLevels(self, root):
    if not root: return []
    bfs, res = [root], []
    while bfs:
        cur_row = [node.val for node in bfs]
        res.append(sum(cur_row)*1.0/len(cur_row))
        bfs = [kid for p in bfs for kid in (p.left,p.right) if kid]
    return res
