class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        longest = 0
        for left in range(len(s)):
            seen = {}
            curlen = 0
            for right in range(left, len(s)):
                cur = s[right]
                
                if cur not in seen:
                    curlen += 1
                    seen[cur] = True
                    longest = max(longest, curlen)
                else:
                    break
        return longest