def binary_searche(l, r):
    while l < r:
        m = l + (r - l) // 2
        if f(m):    # 判断找了没有，optional
            return m
        if g(m):
            r = m   # new range [l, m)
        else:
            l = m + 1 # new range [m+1, r)
    return l    # or not found
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x + 1
        # [left, right)
        while left < right:
            mid = left + (right - left) / 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left - 1
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x + 1 #[left, right)
        while left < right:
            mid = (left + right) / 2
            if mid ** 2 == x:
                return mid
            elif (mid - 1) ** 2 < x and mid ** 2 >= x:
                return mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        return left
