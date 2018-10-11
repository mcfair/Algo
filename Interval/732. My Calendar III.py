#error after passed 74/98 test cases
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
        
