class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        slist, tlist = list(s), list(t)
        slist.sort()
        tlist.sort()
        for i in range(len(slist)):
            if slist[i] != tlist[i]:
                return tlist[i]
        return tlist[-1]
s = "abcd"
t = "abcde"
p = Solution()
print(p.findTheDifference(s,t))
