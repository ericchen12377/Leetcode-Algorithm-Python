class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word[0].isupper():
            return all(map(lambda w : w.isupper(), word[1:])) or all(map(lambda w : w.islower(), word[1:]))
        else:
            return all(map(lambda w : w.islower(), word[1:]))

p = Solution()
word = 'FlaG'
print(p.detectCapitalUse(word))
word = 'USA'
print(p.detectCapitalUse(word))