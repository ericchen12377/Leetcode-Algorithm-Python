class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        _len = len(S)
        index = -1000000
        ans = [0] * _len
        for i, s in enumerate(S): #from left to right
            if s == C:
                index = i
            ans[i] = abs(i - index)
        index = -100000
        for i in range(_len - 1, -1 , -1): #from right to left
            if S[i] == C:
                index = i
            ans[i] = min(abs(i - index), ans[i]) #update min index
        return ans
S = "loveleetcode"
C = 'e'
p = Solution()
print(p.shortestToChar(S,C))