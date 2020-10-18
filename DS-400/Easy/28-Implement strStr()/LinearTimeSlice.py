class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0
        
        for i in range(len(haystack)):
            if haystack[i]==needle[0] and haystack[i:i+len(needle)] == needle and i+len(needle) < len(haystack):
                return i
        return -1




haystack = "hello"
needle = "ll"
p = Solution()
print(p.strStr(haystack, needle))