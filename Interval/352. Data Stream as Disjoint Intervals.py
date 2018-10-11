"""
thought process:
what's the best data structure to maintain this interval array, such that it has low cost to add numbers.
List will have addNum O(N) and getInterval O(1) --> good design for less write/add and heavy read/query
BST will have addNum O(lgN) and getInterval O(N) --> good design for heavy write and light query
Heap implementation will give O(lgN) addNum and O(NlgN) query.
"""
#List solution O(n) Add, O(1) Query
class SummaryRanges(object):
    def __init__(self):
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

#Heap Solution - Heap is a binary tree, but not a Binary Search Tree
class SummaryRanges(object):
    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        heapq.heappush(self.intervals, (val, Interval(val, val)))

    def getIntervals(self):
        stack = []
        while self.intervals:
            idx, cur = heapq.heappop(self.intervals)
            if not stack:
                stack.append((idx, cur))
            else:
                prev = stack[-1][1]
                if cur.start <= prev.end + 1:
                    prev.end = max(prev.end, cur.end)
                else:
                    stack.append((idx, cur))
        self.intervals = stack
        heapq.heapify(self.intervals) #it still works without this line, but why?
        return list(map(lambda x: x[1], stack))


#BST Solution
  
