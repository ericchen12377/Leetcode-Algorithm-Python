import collections
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rcount = collections.Counter(ransomNote)
        mcount = collections.Counter(magazine)
        for r, c in rcount.items():
            if c > mcount[r]:
                return False
        return True
