
#O(logn) - BST   
class Node(object):
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        if end <= self.s:
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
