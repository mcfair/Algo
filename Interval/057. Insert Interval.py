"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
 
        s = newInterval.start
        e = newInterval.end
        
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        
        #this "if" statement handles overlapping intervals
        if len(left) + len(right) != len(intervals):
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
            
        return left + [Interval(s, e)] + right
