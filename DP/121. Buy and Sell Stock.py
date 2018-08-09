#At most one transaction - Another word, find max gap

#keep track of the curmin - 'min price so far'
#curgain = curprice - curmin

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curmin = sys.maxint
        curgain = 0
        for p in prices:
            curmin = min(curmin, p)
            curgain = max(p-curmin, curgain)
        return curgain
