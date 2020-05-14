class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        N = len(prices)
        mins = [0] * N
        maxs = [0] * N
        mins[0] = prices[0]
        for i in range(1, N):
            mins[i] = min(mins[i - 1], prices[i])
        maxs[N - 1] = prices[N - 1]
        for j in range(N - 2, -1, -1):
            maxs[j] = max(maxs[j + 1], prices[j])
        return max(maxs[i] - mins[i] for i in range(N))
p = Solution()
prices = [7,1,5,3,6,4]
print(p.maxProfit(prices))
prices = [7,6,4,3,1]
print(p.maxProfit(prices))