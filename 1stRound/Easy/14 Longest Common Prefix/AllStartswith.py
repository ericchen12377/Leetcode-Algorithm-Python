class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == None or len(strs) == 0:
            return ""
        def is_common(prefix, strs):
            return all(str.startswith(prefix) for str in strs)
        answer = ''
        for i in range(len(strs[0])):
            pre = strs[0][:i + 1]
            print(pre)
            if is_common(pre, strs):
                answer = pre
            else:
                break
        return answer
