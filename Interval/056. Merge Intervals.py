# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class NlgN_Solution(object):
    def merge(self, intervals):

        if not intervals: return []
        intervals.sort(key=lambda x: x.start)

        merged = []
        for i, x in enumerate(intervals):
            if i==0:
                prev_start, prev_end = x.start, x.end
            elif prev_end < x.start:
                merged.append(Interval(prev_start, prev_end))
                prev_start, prev_end = x.start, x.end
            elif prev_end >= x.start:
                prev_end = max(prev_end, x.end)
        merged.append(Interval(prev_start, prev_end))
        return merged
        
#stephan
class NlgN_Solution(object):
    def merge(self, intervals):
        out = []
        for x in sorted(intervals, key=lambda i: i.start):
            if out and x.start <= out[-1].end:
                out[-1].end = max(out[-1].end, x.end)
            else:
                out.append(x)
        return out
