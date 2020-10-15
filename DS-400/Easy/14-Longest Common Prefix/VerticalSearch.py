class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            res = ""
            for j in range(len(strs[0])):
                c = strs[0][j]
                for i in range(1, len(strs)):
                    if(j >= len(strs[i]) or (strs[i][j] != c)):
                        return res 
                res += c
            
            return res






strs = ["flower","flow","flight"]
p = Solution()
print(p.longestCommonPrefix(strs))