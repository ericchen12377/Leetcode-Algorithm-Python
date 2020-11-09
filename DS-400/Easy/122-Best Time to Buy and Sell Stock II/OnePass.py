
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mp = 0
        days = len(prices)
        for i in range(1, days):
            if prices[i] > prices[i-1]:
                mp += prices[i] - prices[i-1]
        return mp