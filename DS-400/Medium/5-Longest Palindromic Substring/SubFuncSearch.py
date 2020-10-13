class Solution(object):
    def LongestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        n = len(s)
        maxlen = 0
        start = 0

        def searchPalindrome(s, left, right, start, maxlen):
            while left >= 0 and right <= len(s) and s[left] == s[right]:
                left-=1
                right+=1
            if maxlen < right - left -1:
                start = left + 1
                maxlen = right - left - 1
            return start, maxlen
        
        for i in range(n-1):
            start, maxlen = searchPalindrome(s, i, i, start, maxlen)
            start, maxlen = searchPalindrome(s, i, i + 1, start, maxlen)
            print(s[start:(start + maxlen)])
        
        return s[start:(start + maxlen)]


        
s = "babaabad"
p = Solution()
print(p.LongestPalindrome(s))