class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        M, N = len(haystack), len(needle)
        for i in range(M - N + 1):
            if haystack[i : i + N] == needle:
                return i
        return -1
haystack = "hello"
needle = "ll"
p = Solution()
print(p.strStr(haystack, needle))