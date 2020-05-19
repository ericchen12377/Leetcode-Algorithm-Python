import collections
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = collections.Counter(deck)
        X = min(count.values())
        for x in range(2, X + 1):
            if all(v % x == 0 for v in count.values()):
                return True
        return False
