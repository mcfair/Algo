"""
This is a classical DP problem. Solve it with BFS+Heap for fun. 
More importantly, the method below is easily extended to backtrack path. 
"""

class Solution(object):
    def minPathSum(self, grid):

        m, n = len(grid), len(grid[0])
        visited = set([])
        q = [(grid[0][0], 0, 0)]
         
        while q:
            cur_path_cost, x,y = heapq.heappop(q) 
            # Cell already visited with lower path_cost
            if (x,y) in visited:
                continue
            else:
                visited.add((x,y))

            # Found target
            if x==m-1 and y==n-1:
                return cur_path_cost
                
            # Go down only if there is still room to go down
            if x < m-1:
                heapq.heappush(q, (cur_path_cost + grid[x+1][y], x+1, y))
                
            # Go right
            if y < n-1:
                heapq.heappush(q, (cur_path_cost + grid[x][y+1], x, y+1))
                
        return -1
        
        
"""
path backtracking with slight modification
it can also track index position instead of value
"""
class Solution(object):
    def minPathSum(self, grid):

        m, n = len(grid), len(grid[0])
        visited = set([])
        start = grid[0][0]
        q = [(start, 0, 0, [start])]
         
        while q:
            cur_path_cost, x,y, path = heapq.heappop(q) 
            # Cell already visited with lower path_cost
            if (x,y) in visited:
                continue
            else:
                visited.add((x,y))

            # Found target
            if x==m-1 and y==n-1:
                return cur_path_cost
                
            # Go down only if there is still room to go down
            if x < m-1:
                heapq.heappush(q, (cur_path_cost + grid[x+1][y], x+1, y, path+[grid[x+1][y]]))
                
            # Go right
            if y < n-1:
                heapq.heappush(q, (cur_path_cost + grid[x][y+1], x, y+1, path+[grid[x][y+1]]))
                
        return -1
