class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        strs.sort()
        size = min(len(strs[0]), len(strs[-1]))
        i = 0
        while i < size and strs[0][i] == strs[-1][i]:
            i += 1
        return strs[0][:i]
