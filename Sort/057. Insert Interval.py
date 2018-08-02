
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
        
        if len(left) + len(right) != len(intervals):
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
            
        return left + [Interval(s, e)] + right
