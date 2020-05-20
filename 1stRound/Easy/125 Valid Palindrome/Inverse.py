class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isValid = lambda x : x == x[::-1]
        string = ''.join([x for x in s.lower() if x.isalnum()])
        return isValid(string)
s = "A man, a plan, a canal: Panama"
p = Solution()
print(p.isPalindrome(s))