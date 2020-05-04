import collections
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        subs = "1234567890"
        licensePlate = licensePlate.replace(" ", "").lower()
        for sub in subs:
            licensePlate = licensePlate.replace(sub, "")
        res = ""
        plateCount = collections.Counter(licensePlate)
        for word in words:
            match = True
            wordCount = collections.Counter(word)
            for w, c in plateCount.items():
                if c > wordCount[w]:
                    match = False
            if (not res or len(res) > len(word)) and match:
                res = word
        return res
