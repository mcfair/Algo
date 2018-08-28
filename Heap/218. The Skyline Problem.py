#The first methed is called "Sweep Line Method", basically scan from left to right.
#Note the input list is already sorted in ascending order by the left x position Li.

import collections
import heapq
import operator

class Solution(object):
    HeightAndRight = collections.namedtuple('HeightAndRight', ['neg_h', 'right'])

    def getSkyline(self, b):
        # T(n) = O(n*log(n))
        # S(n) = O(n)
        
        max_heap, skyline = [], []
        i, n = 0, len(b)
        
        #sort the coordinates of all entering and exiting points, 
        #which are potential critical points
        #removing duplicated x will help the speed litlle bit
        x_positions = sorted(list(set(
            map(operator.itemgetter(0), b) +
            map(operator.itemgetter(1), b)
        ) ))
        
        #traverse all x from left to right
        #main a max_heap which contains "HeightAndRight", the coordinate of exit points 
        #"i" is the pointer to track buildings
        for x in x_positions:
            
            #keep removing the buildings whose ending coordinate is less than x,
            #because buildings on the left are not relavent anymore.
            #The while loop helps to find the tallest building that is on the right of x
            while max_heap and max_heap[0].right <= x:
                heapq.heappop(max_heap)
                
            #For buildings start at position x, push their (-height, right) to max_heap
            while i < n and b[i][0] == x:
                heapq.heappush(max_heap, self.HeightAndRight(-b[i][2], b[i][1]))
                i += 1
            
            #Find the max height h
            h = -max_heap[0].neg_h if max_heap else 0
            
            #[x,h] is the critical point if last building doesn't end at the same height
            if not skyline or skyline[-1][1] != h:
                skyline.append([x, h])
            
            print max_heap
            print skyline
        
        return skyline

#48ms
#https://leetcode.com/problems/the-skyline-problem/discuss/124354/Python-87ms-beats-100-with-explanation
"""
Nearly the same method as '715. Range Module', regarding each building [l, r, h] as an interval [l, r). Use a list axis to record the positions of l and r. Use a list heights to record the height of the right-hand side of the position in axis with the same index. For example, heights[i] records the height between axis[i] and axis[i + 1], that is, the height on interval [axis[i], axis[i + 1]).

First sort buildings by heights, and initialize axis and heights.
Then for each building [l, r, h] we update the two lists following the rules:

Find the indices of l and r in axis, called idl and idr. Then the range we are to update is [idl: idr].
Since the current building is higher than or equal to anyone before it, the height of the right-hand side of l, that is heights[idl], should be h after updated. Meanwhile the height of the right-hand side of r wouldn't change after updated. That is, heights[idr] should be current heights[idr - 1] after updated.
If h != heights[idl - 1], renew axis[idl: idr] = [l, r] and heights[idl: idr] = [h, heights[idr - 1]].
Otherwise h == heights[idl - 1], it means there's a recorded building with height h whose left edge is less than l, hence we don't need to record l. If else idl == idr, it implies there's a recorded building with height h whose right edge is larger than r, then we don't renew anything. Otherwise we only record r and renew axis[idl: idr] = [r] and heights[idl: idr] = [heights[idr - 1]].
After iteration, axis and heights record coordinates of all desired points in order.
"""
class Solution(object):
    def getSkyline(self, buildings):
        
        buildings.sort(key = lambda x:x[2])
        axis = [float('-inf'),float('inf')]
        heights = [0,0]
        
        for l,r,h in buildings:
            idl = bisect.bisect_left(axis, l)
            idr = bisect.bisect_right(axis, r)
            
            if h != heights[idl - 1]:
                axis[idl :idr] = [l, r]
                heights[idl :idr] = [h, heights[idr - 1]]
                
            elif idr > idl:
                axis[idl :idr] = [r]
                heights[idl :idr] = [heights[idr - 1]]
            
        return [[axis[i],heights[i]] for i in range(1,len(axis) - 1)]
        
