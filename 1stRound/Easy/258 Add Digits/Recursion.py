class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            temp = 0
            while num:
                temp += num % 10
                num //= 10
            num = temp
        return num
num = 38
p = Solution()
print(p.addDigits(num))