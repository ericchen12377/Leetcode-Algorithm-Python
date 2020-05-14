class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = 0
        for i, w in enumerate(word):
            if w.isupper():
                count += 1
        return count == len(word) or count == 0 or (word[0].isupper() and count == 1)
p = Solution()
word = 'FlaG'
print(p.detectCapitalUse(word))
word = 'USA'
print(p.detectCapitalUse(word))