class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mp = 0
        buy, sell = 0,1
        days = len(prices)
        while buy < days - 1:
            while buy + sell < days:
                if (prices[buy + sell] - prices[buy]) > mp:
                    mp = prices[buy + sell] - prices[buy]
                sell += 1
            buy += 1
            sell = 1
        return mp



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mp = 0
        days = len(prices)
        for i in range(days -1):
            for j in range(i+1, days):
                if prices[j] - prices[i] > mp:
                    mp = prices[j] - prices[i]
        return mp
            