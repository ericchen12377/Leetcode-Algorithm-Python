class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        sp = 0
        res = 0
        for gi in g:
            while sp < len(s) and s[sp] < gi:
                sp += 1
            if sp < len(s) and s[sp] >= gi:
                res += 1
                sp += 1
        return res
