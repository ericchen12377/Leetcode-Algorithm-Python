class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
haystack = "hello"
needle = "ll"
p = Solution()
print(p.strStr(haystack, needle))