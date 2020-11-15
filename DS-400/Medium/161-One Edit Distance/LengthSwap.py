class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lens = len(s)
        lent = len(t)
        
        if lens < lent:
            tmp = t
            t = s
            s = tmp
        lens = len(s)
        lent = len(t)
        if lens - lent >= 2:
            return False
        elif lens - lent == 1:
            for i in range(lent):
                if s[i] != t[i]:
                    return s[(i+1):] == t[i:]
            return True
        elif lent == lens:
            count = 0
            for i in range(lens):
                if s[i] != t[i]:
                    count+=1 
            return count == 1
            