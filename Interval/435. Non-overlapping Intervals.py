"""
thought process: 
Can Greedy algo guarentte the min # of intervals to remove? No
No matter what, you have to sort it first.
After sort, Can Greedy algo guarentte the min # of intervals to remove? yes

Another thought, typically, when we see "min/max number" type of questions, it smells like DP.
But for this problem, it is unlike to beat O(nlgn) with DP.
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
                pass #Do not append means removal
            
        return len(intervals) - len(stack)
        
#we can optimize for space, since only thing matters is stack[-1].end
class Solution(object):
    def eraseOverlapIntervals(self, intervals):

        intervals.sort(key=lambda x: (x.start, -x.end))
        prev_end = -float('inf')
        removed = 0
        
        for inter in intervals:
            #print inter.start, inter.end, removed, 'prev_end', prev_end
            if  prev_end <= inter.start:
                prev_end = inter.end
            elif inter.end <= prev_end:
                removed +=1
                prev_end = inter.end
            else:
                removed +=1
        return removed
        
