class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        if len(costs) == 1:
            return min(costs[0])
        rows = len(costs)
        dp = costs
        for i in range(1, rows):
            for j in range(3):
                if j == 0: #red
                    dp[i][j] += min(dp[i-1][j+1], dp[i-1][j+2])
                elif j == 1: #blue
                    dp[i][j] += min(dp[i-1][j-1], dp[i-1][j+1])
                elif j == 2:
                    dp[i][j] += min(dp[i-1][j-1], dp[i-1][j-2])
        return min(dp[-1])


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not len(costs):
            return 0
        lastR, lastG, lastB = costs[0][:]
        for i in range(1, len(costs)):
            curR = min(lastG, lastB) + costs[i][0]
            curG = min(lastR, lastB) + costs[i][1]
            curB = min(lastR, lastG) + costs[i][2]
            lastR, lastG, lastB = curR, curG, curB
        
        return min(min(lastR, lastG), lastB)