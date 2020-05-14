class Solution(object):
    def selfDividingNumbers(self, left, right):
        is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
        return list(filter(is_self_dividing, range(left, right + 1)))
left = 1
right = 22
p = Solution()
print(p.selfDividingNumbers(left,right))