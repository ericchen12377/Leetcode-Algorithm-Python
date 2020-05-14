class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        S = S + "A"
        groups = []
        previndex, prevc = 0, ""
        for i, c in enumerate(S):
            if not prevc:
                prevc = c
                previndex = i
            elif prevc != c:
                if i - previndex >= 3:
                    groups.append([previndex, i - 1])
                previndex = i
                prevc = c
        return groups
