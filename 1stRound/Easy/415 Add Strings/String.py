class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        carry = 0
        M, N = len(num1), len(num2)
        if M < N:
            num1 = "0" * (N - M) + num1
        else:
            num2 = "0" * (M - N) + num2
        N = max(M, N)
        for i in range(N - 1, -1, -1):
            add = int(num1[i]) + int(num2[i]) + carry
            if add >= 10:
                carry = 1
                add -= 10
            else:
                carry = 0
            res = str(add) + res
        if carry:
            res = "1" + res
        return res
num1 = '100'
num2 = '200'
p = Solution()
print(p.addStrings(num1,num2))