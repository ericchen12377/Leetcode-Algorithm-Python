import collections
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        res = 0
        prime = 0
        for k, v in count.items():
            if v % 2 == 1: #add odd - 1
                res += v - 1
                prime = 1
            else:
                res += v  #add even
        return res + prime


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
            
        dic = collections.Counter(s)
        count = 0
        check_odd = 0
        for key in dic:
            if dic[key] % 2 == 0:
                count += dic[key]
            elif dic[key] % 2 == 1:
                count += dic[key] - 1
                check_odd = 1
        return count + check_odd