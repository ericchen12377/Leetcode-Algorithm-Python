import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqrt = int(math.sqrt(area))
        for w in range(sqrt, 0, -1):
            if area % w == 0:
                return [area / w, w]
        return [area, 1]
