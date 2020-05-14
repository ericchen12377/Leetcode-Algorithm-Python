class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        moorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans = lambda x: moorse[ord(x) - ord('a')]
        map_word = lambda word: ''.join([trans(x) for x in word])
        res = list(map(map_word, words))
        return len(set(res))

words = ["gin", "zen", "gig", "msg"]
p = Solution()
print(p.uniqueMorseRepresentations(words))