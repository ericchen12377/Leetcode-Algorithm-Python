class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        left, right = 0, N - 1
        slist = list(S)
        while left < right:
            while left < N and (not S[left].isalpha()):
                left += 1
            while right >= 0 and (not S[right].isalpha()):
                right -= 1
            if left < N and right >= 0 and left < right:
                slist[left], slist[right] = slist[right], slist[left]
            left, right = left + 1, right - 1
        return "".join(slist)
S = "a-bC-dEf-ghIj"
p = Solution()
print(p.reverseOnlyLetters(S))