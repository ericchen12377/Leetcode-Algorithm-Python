class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right + 1):
            if self.isDividing(num):
                res.append(num)
        return res
        
    def isDividing(self, num):
        temp = num
        while temp:
            div = temp % 10
            if not div or num % div != 0:
                return False
            temp //= 10
        return True
left = 1
right = 22
p = Solution()
print(p.selfDividingNumbers(left,right))