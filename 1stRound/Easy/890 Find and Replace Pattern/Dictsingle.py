class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if len(word) != len(pattern): continue
            d = dict()
            isMatch = True # initial the indicator to be true
            for i, c in enumerate(pattern):
                if c in d:
                    if d[c] != word[i]:
                        isMatch = False #check if match pattern to word
                        break
                d[c] = word[i]
            d = dict()
            for i, c in enumerate(word):
                if c in d:
                    if d[c] != pattern[i]:
                        isMatch = False #check for both word to pattern
                        break
                d[c] = pattern[i]
            if isMatch:
                res.append(word)
        return res
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
p = Solution()
print(p.findAndReplacePattern(words, pattern))