class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        def minCost(i, cost):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return cost[i]
            return cost[i] + min(minCost(i-1, cost), minCost(i-2, cost))
        return min(minCost(n-1, cost), minCost(n-2, cost))

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        dp = [0] * (n + 1)
        def minCost(i, cost, dp):
            if i < 0:
                return 0
            if i == 0 or i == 1:
                return cost[i]
            dp[i] = cost[i] + min(minCost(i-1, cost, dp), minCost(i-2, cost, dp))
            return dp[i]
        return min(minCost(n-1, cost, dp), minCost(n-2, cost, dp))