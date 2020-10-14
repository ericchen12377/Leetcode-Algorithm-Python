import re
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        s = re.findall('(^[\+\-0]*\d+)\D*', s)

        try:
            result = int(''.join(s))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0




s =  "-987"
p = Solution()
print(p.myAtoi(s))