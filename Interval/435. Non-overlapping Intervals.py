"""
thought process: 
Can Greedy algo guarentte the min # of intervals to remove? No
No matter what, you have to sort it first.
After sort, Can Greedy algo guarentte the min # of intervals to remove? yes
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):

        intervals.sort(key=lambda x: (x.start, -x.end))
        stack = []
        for inter in intervals:
            if not stack or stack[-1].end <= inter.start:
                stack.append(inter)
            elif inter.end <= stack[-1].end:
                stack.pop()
                stack.append(inter)
            else: 
                pass
            
        return len(intervals) - len(stack)
        
