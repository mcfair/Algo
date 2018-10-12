#BST error after passed 74/98 test cases
class MyCalendarThree(object):
    def __init__(self):
        self.root = None
        self.maxbooked = 0

    def book(self, start, end):
        self.root = self.insert(start, end, self.root)
        return self.maxbooked
        
    def insert(self, start, end, root):
        if not root:
            root = Node(start, end)
            self.maxbooked = max(root.overlap, self.maxbooked)
            return root

        if start >= end:
            return root

        if root.end<=start:
            root.right = self.insert(start, end, root.right)
            self.maxbooked = max([root.overlap, root.right.overlap, self.maxbooked])

        elif end <= root.start:
            root.left = self.insert(start, end, root.left)
            self.maxbooked = max([root.overlap, root.left.overlap, self.maxbooked])
        else:
            root.overlap +=1
            a = min(root.start, start)
            b = max(root.start, start)
            c = min(root.end, end)
            d = max(root.end, end)
            root.start, root.end = b, c
            root.left = self.insert(a, b, root.left)
            root.right= self.insert(c, d, root.right)
            self.maxbooked = max([root.overlap, root.left.overlap, root.right.overlap, self.maxbooked])
        return root
        
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.overlap = 1   
        
        
#Another idea is Segment Tree
class MyCalendarThree(object):
    def __init__(self):
        self.st = SegTree()

    def book(self, start, end):
        self.st.add(start, end)
        return self.st.v[1]
    
class SegTree(object):
    def __init__(self):
        self.v = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)
 
    def add(self, s, e, l = 0, r = 10**9+1, id = 1):
        if s >= r or e <= l: return
        if s <= l < r <= e:
            self.lazy[id] += 1
            self.v[id] += 1
            return
        m = (l + r) // 2
        self.add(s, e, l, m, id * 2)
        self.add(s, e, m, r, id*2+1)
        self.v[id] = self.lazy[id] + max(self.v[id*2], self.v[id*2+1])
            

