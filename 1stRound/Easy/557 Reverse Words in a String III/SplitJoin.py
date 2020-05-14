class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(map(lambda x : x[::-1], s.split(" ")))
s = "Let's take LeetCode contest"
p = Solution()
print(p.reverseWords(s))