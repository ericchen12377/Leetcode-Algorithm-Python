import collections
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sCount = collections.Counter(S)
        res = 0
        for j in J:
            res += sCount[j]
        return res
J = "aA"
S = "aFFAAdD"
p = Solution()
print(p.numJewelsInStones(J,S))