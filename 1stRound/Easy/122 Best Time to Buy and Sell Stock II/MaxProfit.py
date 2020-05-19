class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        ans = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                ans += prices[i + 1] - prices[i]
        return ans
