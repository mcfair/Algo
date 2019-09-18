BFS + Heap, and Dijkstra is just part of it


Dijkstra Algorithm to find the shortest path for weighted graph (directed or undirected)

Time complexity: O(E+NlogN)
The code below is very powerful for followup questions, it returns (1)totalPrice, (2)numStops, and (3)path from src to dst.

```python
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        g = collections.defaultdict(dict)
        for u, v, price in flights:
            g[u][v] = price
            
        #tuple inside heap represents (totalPrice, numStops, node, path)
        heap = [(0, 0, src, [src])] 
        while heap:
            price, stops, i, path = heapq.heappop(heap)
            if i == dst:
                return price
            if stops<=K:
                for j in g[i]:      
                    if j not in path:
                        heapq.heappush(heap, (price+g[i][j], stops+1, j, path+[j]))
                      
        return -1
```
