class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        if len(costs) == 1:
            return min(costs[0])
        def dfs(costs, prev):
            if not costs:
                return 0
            r = b = g = float("inf")
            if prev != "red":
                r = costs[0][0] + dfs(costs[1:], "red")
            if prev != "blue":
                b = costs[0][1] + dfs(costs[1:], "blue")
            if prev != "green":
                g = costs[0][2] + dfs(costs[1:], "green")
            return min(r, b, g)
        return dfs(costs, "")