class SegmentTree:
    class SegmentTreeNode:
        def __init__(self, l, r, val=0):
            self.l = l
            self.r = r
            self.left = self.right = None
            self.lazy = 0
            self.val = val

    def __init__(self, l, r):
        self.root = self.SegmentTreeNode(l, r, 0)

    def normalize(self, node):
        if node.lazy != 0:
            node.val += node.lazy

        if node.l < node.r:
            if not node.left or not node.right:
                mid = (node.l + node.r) // 2
                node.left = self.SegmentTreeNode(node.l, mid, node.val)
                node.right = self.SegmentTreeNode(mid, node.r, node.val)
            else:
                node.left.lazy += node.lazy
                node.right.lazy += node.lazy

        node.lazy = 0

    def query(self, start, end):
        return self._query(start, end, self.root)

    def _query(self, start, end, node):
        self.normalize(node)

        if start >= end or not node or node.l >= end or node.r <= start:
            return 0

        if start <= node.l and node.r <= end:
            return node.val

        return max(self._query(start, end, node.left), self._query(start, end, node.right))


    def update(self, start, end):
        return self._update(start, end, self.root, 1)

    def _update(self, start, end, node, val):
        self.normalize(node)
        if start >= end or not node or node.l >= end or node.r <= start:
            return

        if start <= node.l and node.r <= end:
            node.lazy = val
            self.normalize(node)
            return
        else:
            self._update(start, end, node.left, val)
            self._update(start, end, node.right, val)

        node.val = max(node.left.val, node.right.val)
        
class MyCalendarTwo:
    def __init__(self):
        self.sTree = SegmentTree(0, 10**9+1)

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        count = self.sTree.query(start, end)
        
        if count >= 2:
            return False
        
        self.sTree.update(start, end)
        return True 
