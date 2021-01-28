class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        M = float('inf')
        # dynamic programming
        dp = [0] + [M] * amount
        for i in range(1, amount+1):
            dp[i] = 1 + min([dp[i-c] for c in coins if i >= c] or [M])
        return dp[-1] if dp[-1] < M else -1
