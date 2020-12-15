class WordDistance:

    def __init__(self, words):
        self.words = words
        
    def shortest(self, word1, word2):
        cur = float('Inf')
        a, b = -1,-1
        
        for index, word in enumerate(self.words):
            if word  == word1:
                a = index
                if b > -1:
                    cur = min(cur, abs(a-b))
            if word == word2:
                b = index
                if a > -1:
                    cur = min(cur, abs(a-b))
                
        return cur


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)