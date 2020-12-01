class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(s):
            return s == s[::-1]

        if is_palindrome(s):
            return True
        
        if len(s) <= 1:
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left:right]) or is_palindrome(s[left + 1:right + 1])
            else:
                left += 1
                right -= 1
        return False
            
                
        
        