class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        
        dp = [0] * (len(cost) + 1)
        cost.append(0)
        dp[0] = cost[0]
        dp[1] = cost[1]
        n = 2
        while n < len(cost):
            dp[n] = min(dp[n-1], dp[n-2]) + cost[n]
            n += 1
        return dp[n-1]
        


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*n
        dpOne = cost[0]
        dpTwo = cost[1]
        
        for i in range(2,n):
            current = cost[i] + min(dpOne, dpTwo)
            dpOne = dpTwo
            dpTwo = current
        return min(dpOne, dpTwo)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*len(cost)
        
        for i in range(n):
            if i < 2:
                print(i)
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])