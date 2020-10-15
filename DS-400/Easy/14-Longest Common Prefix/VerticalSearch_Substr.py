class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            for j in range(len(strs[0])):
                c = strs[0][j]
                for i in range(1, len(strs)):
                    if(j >= len(strs[i]) or (strs[i][j] != c)):
                        return strs[i][0:j]
            
            return strs[0]






strs = ["flower","flow","flight"]
p = Solution()
print(p.longestCommonPrefix(strs))