class MyCalendarThree(object):
    def __init__(self):
        self.root = SegTree()

    def book(self, start, end):
        self.root.add(start, end)
        return self.root.v[1]
    
class SegTree(object):
    def __init__(self):
        self.v = collections.defaultdict(int)
        self.lazy = collections.defaultdict(int)
 
    def add(self, s, e, l = 0, r = 10**9+1, id = 1):
        if s >= r or e <= l: 
            return
        if s <= l < r <= e:
            self.lazy[id] += 1
            self.v[id] += 1
            return
        m = (l + r) // 2
        self.add(s, e, l, m, id * 2)
        self.add(s, e, m, r, id*2+1)
        self.v[id] = self.lazy[id] + max(self.v[id*2], self.v[id*2+1])
            
