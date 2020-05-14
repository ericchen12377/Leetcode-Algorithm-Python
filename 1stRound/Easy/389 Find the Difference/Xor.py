from functools import reduce
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(lambda x, y : x ^ y, map(ord, s + t)))
s = "abcd"
t = "abcde"
p = Solution()
print(p.findTheDifference(s,t))