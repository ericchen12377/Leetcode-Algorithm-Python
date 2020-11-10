class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
       
        s = re.sub(r"[\W_]+", '',s).lower()
        
        return s == s[::-1]