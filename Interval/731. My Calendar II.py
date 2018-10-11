"""
My Calendar I: if find overlap return False, else insert meeting
My Calendar II: allow double booking, but not triple booking or beyond 
"""
#Fisrt, a short O(n) solution, record double booked time intervals in self.overlaps
class MyCalendarTwo(object):
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        #check if there is already a double booking
        for i, j in self.overlaps:
            if start < j and end > i: 
                return False
        #traverse the calendar to find the overlaped time intervals
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True
    
# BST O(lgN), This code can handle arbitary number of overlaps 
class MyCalendarTwo:
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if not self.is_insertable(start, end, self.root):
            return False

        self.root = self.insert(start, end, self.root)
        return True

    def is_insertable(self, start, end, root):
        if not root:
            return True

        if start >= end:
            return True

        if end <= root.start:
            return self.is_insertable(start, end, root.left)

        elif start >= root.end:
            return self.is_insertable(start, end, root.right)

        else: #overlap
            if root.overlap>=1:
                return False
            elif start >= root.start and end <= root.end:
                return True
            else:
                return self.is_insertable(start, root.start, root.left) and self.is_insertable(root.end, end, root.right)

    def insert(self, start, end, root):
        if not root:
            root = Node(start, end)
            return root

        if start >= end:
            return root

        if start >= root.end:
            root.right = self.insert(start, end, root.right)

        elif end <= root.start:
            root.left = self.insert(start, end, root.left)
        
        else:
            root.overlap +=1
            a = min(root.start, start)
            b = max(root.start, start)
            c = min(root.end, end)
            d = max(root.end, end)
            root.start, root.end = b, c
            root.left, root.right = self.insert(a, b, root.left), self.insert(c, d, root.right)
            
        return root

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.overlap = 0
