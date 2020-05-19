class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        pre = min(strs, key = len)
        for i, c in enumerate(pre):
            for word in strs:
                if word[i] != c:
                    return pre[:i]
        return pre
