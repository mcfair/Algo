"""
thought process:
what's the best data structure to maintain this interval array, such that it has low cost to add numbers.
(1) List will have addNum O(N) and getInterval O(1) --> good design for less write/add and heavy read/query
(2) BST will have addNum O(lgN) and getInterval O(N) --> good design for heavy write and light query
(3) Heap implementation will give O(lgN) addNum and O(NlgN) query.
(4) Union-Find
Think this way:  each point of time is a vertex, consecutive points form a connected component, interval = [min,max].
In typical union-find, all vertices inside a connected component will be able to find its root by recursively calling its parent.
This action is performed when a new vertex comes in, and the there is a need to determine if one of its neighbors belong to an existing component.
But in this problem, a component (aka interval) can only have 2 border nodes (upper/lower bound of a range).
It's only necessary for the border nodes to be able to find the root. Therefore there is no more need to have a find(). 
So a hash table that tracks the border nodes is used instead.
https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/82619/JAVA-AC-Union-Find-Solution
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
  
