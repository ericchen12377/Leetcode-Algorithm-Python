class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 2 **31
        mp = 0
        days = len(prices)
        for i in range(days):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > mp:
                    mp = prices[i] - min_price
        return mp