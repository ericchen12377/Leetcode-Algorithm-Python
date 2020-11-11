class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        if not s:
            return [[]]
        dp = {0:[[]], 1:[[s[0]]]}
        for ii in xrange(1, len(s)):
            dp[ii+1] = []
            for jj in xrange(0, ii+1):
                if self.isPalindrome(s[jj:ii+1]):
                    for sol in dp[jj]:
                        dp[ii+1].append(sol+[s[jj:ii+1]])
        return dp[len(s)]

    
    def isPalindrome(self, string):
        return string == string[::-1]



class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[[]]]
        psi = [0]   # palindrome start indices
        for i, c in enumerate(s):
            psi = [k for k in psi if s[k] == s[i]]
            dp.append([pp + [s[k:i+1]] for k in psi for pp in dp[k]])
            psi = [k-1 for k in psi if k > 0] + [i, i+1]
        return dp[-1]