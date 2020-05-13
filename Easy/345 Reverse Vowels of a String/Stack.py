class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vstack = []
        for c in s:
            if c in "aeiouAEIOU":
                vstack.append(c)
        res = []
        for c in s:
            if c in "aeiouAEIOU":
                res.append(vstack.pop())
            else:
                res.append(c)
        return "".join(res)
