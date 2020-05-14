class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        set_p = set(pattern)
        for word in words:
            if len(set(word)) != len(set_p): #check if the same length
                continue
            fx = dict()
            equal = True
            for i, w in enumerate(word):
                if w in fx:
                    if fx[w] != pattern[i]: #dict of word projected to pattern
                        equal = False
                        break
                fx[w] = pattern[i]
            if equal:
                ans.append(word)
        return ans

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
p = Solution()
print(p.findAndReplacePattern(words, pattern))