class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n + 1 #[left, right)
        while left < right:
            mid = left + (right - left) / 2
            if mid * (mid + 1) / 2 <= n:
                left = mid + 1
            else:
                right = mid
        return left - 1
