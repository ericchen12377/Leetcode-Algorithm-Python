class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        index = -200000
        _len = len(seats)
        ans = [0] * _len
        for i in range(_len):
            if seats[i] == 1:
                index = i
            else:
                ans[i] = abs(i - index)
        index = -200000
        for i in range(_len - 1, -1, -1):
            if seats[i] == 1:
                index = i
            else:
                ans[i] = min(abs(i - index), ans[i])
        return max(ans)
