class Solution(object):
    def maxProfit(self, prices):
        buy = float('inf')
        sell = 0
        for i in prices:
            if i < buy:
                buy = i
            sell = max(sell, i-buy)
        return sell
            

        