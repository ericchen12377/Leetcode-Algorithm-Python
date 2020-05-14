import re
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return not re.match(".*A.*A.*", s) and not re.match(".*LLL.*", s)
p = Solution()
s = "PPALLP"
print(p.checkRecord(s))
s = "PPALLL"
print(p.checkRecord(s))