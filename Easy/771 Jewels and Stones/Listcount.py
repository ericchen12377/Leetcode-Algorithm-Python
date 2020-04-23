class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(S.count(j) for j in J)
J = "aA"
S = "aFFAAdD"
p = Solution()
print(p.numJewelsInStones(J,S))