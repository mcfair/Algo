class SegmentTreeNode(object):
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = start
        self.left = None
        self.right = None

class SegmentTree(object):
    def __init__(self, n):
        self.root = self.buildTree(0, n-1)

    def buildTree(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root
            
        mid = (start+end) / 2
        root.left = self.buildTree(start, mid)
        root.right = self.buildTree(mid+1, end)
        
        return root

    def update(self, i, diff, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return
        root.val += diff    
        if i == root.start == root.end:
            return
            
        self.update(i, diff, root.left)
        self.update(i, diff, root.right)

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0
        if start <= root.start and end >= root.end:
            return root.val
        return self.sum(start, end, root.left) + self.sum(start, end, root.right)
