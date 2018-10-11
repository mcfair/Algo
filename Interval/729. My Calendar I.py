"""
Existing meeting |-------------------|            |--------|
               |----|  or |----|or |------| or  |------------|
conditions can be summarized as start < e and end > s

if we don't keep self.intervals sorted, search takes O(n), append takes O(1)

if we keep it sorted, binary search takes O(lgn) insert takes O(n)

What else we can do to keep both O(lgn) search and O(1) insert? Binary Search Tree
"""
#O(n)
class MyCalendarI:
    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        for s, e in self.intervals:
            if not (start >= e or end <= s): 
            #if start < e and end > s:
                return False
            
        self.intervals.append((start, end))
        return True
        
#O(logn) - BST   
class Node(object):
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        if self.s >= end:
            if self.left is None:
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        elif self.e <= start:
            if self.right is None:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        else:
            return False


class MyCalendar(object):            

    def __init__(self):
        self.root = None
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)
