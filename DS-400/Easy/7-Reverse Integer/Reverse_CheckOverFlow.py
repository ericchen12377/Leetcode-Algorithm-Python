class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -2**31 <= x <= 2**31 - 1:
            res = []
            ind = 1
            if x < 0:
                ind = -1
            size = len(str(abs(x)))
            for i in range(size):
                res.append(abs(x) % 10 * (10 ** (size - i - 1)))
                x = abs(x) // 10
            
            return sum(res) * ind if -2**31 <= sum(res) * ind <= 2**31 - 1 else 0
        else:
            return 0
        





x =  123
p = Solution()
print(p.reverse(x))