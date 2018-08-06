#same code as LC265 paint house II

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        
        n, k = len(costs), len(costs[0])
        
        for i in range(1, n):
            for j in range(k):
                costs[i][j] += min(costs[i-1][:j] + costs[i-1][j+1:])
                
        return min(costs[n-1])
