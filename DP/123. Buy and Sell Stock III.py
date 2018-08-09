#At most two transactions - actually it asks for maxsum of (max-min) of two subsets
#Use the DP technique twice from left to right, then from right to left

#simliar problems: Largest Area Histogram, 3 Non-overlapping continuos sum.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
       
        if len(prices)<=1: return 0
        
        #O(n) counting from left, find the max gain up to each day (not ending at each day)
        left = [0]*len(prices)
        curmin = prices[0]
        for i in range(1, len(prices)):
            curmin = min(curmin, prices[i])
            left[i] = max(prices[i]-curmin, left[i-1])
         
        #O(n) counting from right, find the max gain up to each day
        right = [0]*len(prices)
        curmax = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            curmax = max(curmax, prices[i])
            right[i] = max(curmax-prices[i], right[i+1])
            
        #O(n) varying i to find max(left[i]+right[i])    
        max2t = 0
        for i in range(len(prices)):
            max2t = max(max2t, left[i] + right[i])
        return max2t
        
