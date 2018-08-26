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

    
"""
DP, Bellman-Ford Algorithm
O(N^2*K) time, O(N) space
But this method is not scalalbe to any followup question
"""

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
 
        mp = [float('inf')]*n
        mp[src] = 0
        
        for _ in range(K+1):
            tmp = mp[:]
            for u,v,price in flights:
                tmp[v] = min(tmp[v], mp[u]+price)
            mp = tmp
        return mp[dst] if mp[dst] < float('inf') else -1

 """
 Closing Remarks
 Dijkstra's worst case time complexity is O((|V|+|E|)log|V|), which is O(|V|^2logV) when E = V^2. 
 For Bellman Ford, it's O(|V||E|), which is O(|V|^3).
 """
