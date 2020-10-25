class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if (not s or s.isspace()) else len(s.split()[-1])