class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        groups = []
        before_index, before_char = 0, S[0]
        for i, s in enumerate(S):
            if s != before_char:
                if i - before_index >= 3:
                    groups.append([before_index, i - 1])
                before_index = i
                before_char = s
        if i - before_index >= 2:
            groups.append([before_index, i])
        return groups
