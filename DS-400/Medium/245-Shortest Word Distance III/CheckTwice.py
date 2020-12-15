class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        i1 = -1
        i2 = -1
        minDis = len(words)
        
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
                if i1 != i2 and i2 != -1:
                    minDis = min(minDis, abs(i1-i2))
            if words[i] == word2:
                i2 = i
                if i1 != -1 and i1 != i2:
                    minDis = min(minDis, abs(i1-i2))
        return minDis