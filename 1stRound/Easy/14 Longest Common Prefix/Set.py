class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        pre = ""
        _len = min(len(s) for s in strs)
        for i in range(1, _len + 1):
            if len(set(s[:i] for s in strs)) == 1:
                pre = strs[0][:i]
        return pre
