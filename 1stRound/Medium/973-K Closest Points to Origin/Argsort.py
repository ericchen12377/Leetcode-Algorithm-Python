import numpy as np


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        for p in points:
            d = np.sqrt(p[0]**2 + p[1]**2)
            res.append(d)
        idx = np.argsort(res)[:K]
        print(idx)
        return [points[i] for i in idx]
