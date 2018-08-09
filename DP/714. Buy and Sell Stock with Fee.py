# cash and hold are two results that we could have for one day, and they are INCREASING only.

# cash, 今天套现的最大利润: (1)要么我之前就没买(之前的cash)，(2)要么我之前有股票，但是今天要卖掉；
# 两者选大的作为今天套现的最大利润 

# hold, 今天hold(留/买)的最大利润: (1)要么之前我就有股票，直接用那个利润 (2)要么我之前没有，今天我得买；
# 两者选大的作为我今天要hold股票的最大利润


class Solution(object):
    def maxProfit(self, prices, fee):
        cash = 0   
        hold = cach -prices[0]  
        
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash
