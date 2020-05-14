class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        N = len(digits)
        pos = N - 1
        carry = 0
        digits[-1] += 1 #add one to the last
        while pos >= 0: #loop each other position to carry
            digits[pos] += carry
            if digits[pos] >= 10:
                carry = 1
                digits[pos] -= 10
            else:
                carry = 0
            pos -= 1
        if carry:
            digits.insert(0, 1)
        return digits
digits = [1,9,9]
p = Solution()
print(p.plusOne(digits))