import numpy as np
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            strs = np.sort(strs)
            i = 0
            length = min(len(strs[0]), len(strs[-1]))
            while(i < length and strs[0][i] == strs[-1][i]):
                i += 1
            return strs[0][0:i]






strs = ["flower","flow","flight"]
p = Solution()
print(p.longestCommonPrefix(strs))