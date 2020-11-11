class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordset = set(wordDict)
        dp = [False]*(len(s) + 1)
        dp[0] = True
        
        for i in range(len(dp)):
            for j in range(i):
                print(s[j:(i)])
                if dp[j] and s[j:(i)] in wordset:
                    dp[i] = True
                    break
        return dp[-1]