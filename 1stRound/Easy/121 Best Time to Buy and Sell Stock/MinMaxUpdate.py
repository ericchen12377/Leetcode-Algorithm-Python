class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        res = 0
        minP, maxP = float("inf"), 0
        for i in range(N):
            if minP > prices[i]:
                minP = prices[i]
                maxP = 0
            if maxP < prices[i]:
                maxP = prices[i]
            res = max(res, maxP - minP)
        return res
p = Solution()
prices = [7,1,5,3,6,4]
print(p.maxProfit(prices))
prices = [7,6,4,3,1]
print(p.maxProfit(prices))