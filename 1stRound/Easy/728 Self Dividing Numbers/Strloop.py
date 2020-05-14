class Solution:
    def isDividingNumber(self, num):
        if '0' in str(num):
            return False
        return 0 == sum(num % int(i) for i in str(num)) # check all digits self-dividing
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer = []
        for num in range(left, right+1):
            print(num)
            if self.isDividingNumber(num): # if True, return num
                answer.append(num)
        return answer

left = 1
right = 22
p = Solution()
print(p.selfDividingNumbers(left,right))
