import collections
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        scount, tcount = collections.Counter(s), collections.Counter(t)
        for t in tcount:
            if tcount[t] > scount[t]:
                return t
s = "abcd"
t = "abcde"
p = Solution()
print(p.findTheDifference(s,t))