import collections
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for p0 in points:
            d = collections.defaultdict(int)
            for p1 in points:
                d[(p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2] += 1
            for d, v in d.items():
                res += v * (v - 1)
        return res
