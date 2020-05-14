import collections
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        scount = collections.Counter(s)
        tcount = collections.Counter(t)
        return scount == tcount
