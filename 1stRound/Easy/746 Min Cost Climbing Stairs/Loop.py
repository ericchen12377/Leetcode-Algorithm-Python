class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        costed = [0, 0]
        for i in range(2, len(cost)):
            costed.append(min(costed[i - 1] + cost[i - 1], costed[i - 2] + cost[i - 2]))
        return min(costed[-1] + cost[-1], costed[-2] + cost[-2])
