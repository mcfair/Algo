"""
thought process:
what's the best data structure to maintain this interval array, such that it has low cost to add numbers.
List will have addNum O(n) and getInterval O(1) --> good design for less write/add and heavy read/query
BST will have addNum O(lgn) and getInterval O(n) --> good design for heavy write and light query
"""
#List solution O(n) Add, O(1) Query
class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memo = []
        

    def addNum(self, val):  #this function is directly copied from LC57. Insert Intervals
        """
        :type val: int
        :rtype: void
        """
        left = [i for i in self.memo if i.end < val-1]
        right = [i for i in self.memo if i.start > val+1]
        
        #this "if" statement handles overlapping intervals
        if len(left) + len(right) != len(self.memo):
            s = min(val, self.memo[len(left)].start)
            e = max(val, self.memo[~len(right)].end)
            self.memo = left + [Interval(s, e)] + right
        else:
            self.memo = left + [Interval(val,val)] + right
            
    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.memo

   #BST Solution
  
