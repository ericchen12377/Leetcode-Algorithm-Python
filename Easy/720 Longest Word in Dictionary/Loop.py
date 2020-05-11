class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wset = set(words)
        res = ""
        for w in words:
            isIn = True
            for i in range(1, len(w)): #check if all subwords in 
                if w[:i] not in wset:
                    isIn = False
                    break
            if isIn:
                if not res or len(w) > len(res): #check if longest
                    res = w
                elif len(w) == len(res) and res > w: #check if order 
                    res = w
        return res
