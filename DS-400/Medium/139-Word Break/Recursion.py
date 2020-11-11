class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordset = set(wordDict)
        #memo is whether s[i,len(s)-1] can be splitted
        memo = [-1] * len(s)
        
        def check(s, wordset, start, memo):
            if start >= len(s):
                return True
            if memo[start] != -1:
                return memo[start]
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordset and check(s, wordset, end, memo):
                    memo[start] = 1
                    return True
                else:
                    memo[start] = 0
            return False
        return check(s, wordset, 0, memo)