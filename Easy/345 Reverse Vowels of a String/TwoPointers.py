class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        res = list(s)
        left, right = 0, N - 1
        while left < right:
            while right >= 0 and res[right] not in "aeiouAEIOU":
                right -= 1
            while left < right and res[left] not in "aeiouAEIOU":
                left += 1
            if left < right:
                res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
        return "".join(res)
