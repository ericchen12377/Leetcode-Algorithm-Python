class Solution(object):
    def LongestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        n = len(s)
        length = 1
        start = 0
        dp = [[0] * (n) for _ in range(n)]
        for i in range(n):
            print(i)
            dp[i][i] = 1
            for j in range(i):
                dp[j][i] = (s[i]==s[j]) and (i - j < 2 or dp[j+1][i-1])
                print(dp[j][i])
                if (dp[j][i]) and (length < i - j + 1):
                    length = i - j + 1
                    start = j 

        return s[start:(start + length)]


        
s = "babaabad"
p = Solution()
print(p.LongestPalindrome(s))

