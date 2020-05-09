class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        N = len(cost)
        cost.append(0)
        dp = [0] * (N + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, N + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[-1]
