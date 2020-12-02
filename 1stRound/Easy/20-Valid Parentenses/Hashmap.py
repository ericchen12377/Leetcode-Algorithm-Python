class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        bmap = {"(": ")", "[": "]",  "{": "}"}
        if not s:
            return True
        stack = []
        for i in range(len(s)):
            if s[i] in bmap:
                stack.append(s[i])
            else:
                if stack:
                    leftbracket = stack.pop()
                    correctbracket = bmap[leftbracket]
                    if s[i] != correctbracket:
                        return False
                else:
                    return False
        return stack == []
        