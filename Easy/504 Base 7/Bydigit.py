class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"
        res = []
        sign =  num >= 0
        num = abs(num)
        while num != 0:
            res.append(num % 7)
            num //= 7
        return ("" if sign else "-") + "".join(map(str, res[::-1]))
