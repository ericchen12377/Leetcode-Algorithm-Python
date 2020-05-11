class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        tests = minutesToTest / minutesToDie + 1 #how many test one pig can do
        pigs = 0
        while tests ** pigs < buckets: #count till more than buckets
            pigs += 1
        return pigs
