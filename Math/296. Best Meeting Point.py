"""
Best Meeting Point https://leetcode.com/problems/best-meeting-point/

Median minimizes the absolute distance of points: O(MN)

Median minimizes the absolute distance of points. Mean minimizes the squared distance from points.
http://math.stackexchange.com/questions/113270/the-median-minimizes-the-sum-of-absolute-deviations?rq=1
We simply find the list of x and y co-ordinates where we have a building. Then we individually sort them to find the median element in each list. This is the point which is closest meeting point.
To find the total walking distance, simply add abs(x_median-x) and abs(y_median-y) to the final result. Note it doesnt matter that we sorted the co-ordinate lists since the order in which we add does not matter.
"""

class Solution(object):
    def minTotalDistance(self, grid):
        if not grid: return 0
        r, c = len(grid), len(grid[0]) 
        
        #find (x,y) positions of 1's
        rpos, cpos = [], [] 
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    rpos.append(i)
                    cpos.append(j)
        rpos.sort()
        cpos.sort()
        #find the median position
        mid_row = rpos[len(rpos)/2]
        mid_col = cpos[len(cpos)/2]
        
        rdist = sum([abs(r-mid_row) for r in rpos])
        cdist = sum([abs(c-mid_col) for c in cpos])
        return  rdist + cdist 
