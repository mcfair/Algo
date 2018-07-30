# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        
        #O(nlogn)
        intervals.sort(key=lambda x: x.start)
        
        hq, nrooms = [-1], 1
        #O(nlogk) k is the max len of the heap
        for meeting in intervals:
            s, e = meeting.start, meeting.end
            if s >= hq[0]: #reuse a room
                heapq.heappushpop(hq, e)
            else:
                nrooms +=1
                heapq.heappush(hq, e)
        return nrooms
