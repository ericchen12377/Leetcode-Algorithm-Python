class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        longest = 0
        left = 0
        seen = {}
        
        for right in range(len(s)):
            if s[right] in seen:
                left = max(seen[s[right]], left)
            longest = max(longest, right - left + 1)
            seen[s[right]] = right + 1 #+1 gives the window
        return longest