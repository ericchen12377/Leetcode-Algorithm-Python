class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        if num == 1: return True
        if num % 4 == 0:
            return self.isPowerOfFour(num // 4)
        return False

num = 16
p = Solution()
print(p.isPowerOfFour(num))