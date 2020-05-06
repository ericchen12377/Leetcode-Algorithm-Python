class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        minPrice = float('inf')
        profit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            profit = max(profit, price - minPrice)
        return profit
p = Solution()
prices = [7,1,5,3,6,4]
print(p.maxProfit(prices))
prices = [7,6,4,3,1]
print(p.maxProfit(prices))