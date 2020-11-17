class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        slow, fast = 0,0
        s[:] = s[::-1]
        for i in range(len(s)):
            if s[i] != " ":
                fast += 1
            elif s[i] == " ":
                print(s[slow:fast])
                s[slow:fast] = s[slow:fast][::-1]
                print(s[slow:fast])
                slow, fast = i+1,i+1
        s[slow:fast] = s[slow:fast][::-1]
        return s
            
        