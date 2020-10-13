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

        for i in range(n):
            if(n - i <= maxlen / 2):
                break
                print(s[start:maxlen])
            else:
                left = i
                right = i
                while right < n - 1 and s[right + 1] == s[right]:
                    right+=1
                # i = right + 1
                while left > 0 and right < n - 1 and s[right + 1] == s[left - 1]:
                    right+=1
                    left-=1
                print('left', left)
                print('right', right)
                print('maxlen', maxlen)
                if maxlen < right - left + 1:
                    maxlen = right - left + 1
                    start = left
                    print(s[start:(start + maxlen)])
        return s[start:(start + maxlen)]


        
s = "babaabad"
p = Solution()
print(p.LongestPalindrome(s))