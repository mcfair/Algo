Dijkstra Algorithm to find the shorted path for weighted graph (directed or undirected)

```
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):

        g = collections.defaultdict(dict)
        for u, v, price in flights:
            g[u][v] = price
        
        heap = [(0, 0, src)] #(totalPrice, numStops, node)
        while heap:
            price, stops, i = heapq.heappop(heap)
            if i == dst:
                return price
            if stops<=K:
                for j in g[i]:
                    heapq.heappush(heap, (price+g[i][j], stops+1, j))
    return -1
```
