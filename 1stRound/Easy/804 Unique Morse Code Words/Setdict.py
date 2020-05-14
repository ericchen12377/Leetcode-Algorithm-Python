class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        edict = dict(zip(english, morse))
        res = set()
        for word in words:
            mword = ""
            for w in word:
                mword = mword + edict[w]
            res.add(mword)
        return len(res)
        
words = ["gin", "zen", "gig", "msg"]
p = Solution()
print(p.uniqueMorseRepresentations(words))