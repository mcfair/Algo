"""
O(E+NlogN)
This code is very powerful for followup questions, it returns totalPrice, numStops, and path from src to dst.
"""
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
