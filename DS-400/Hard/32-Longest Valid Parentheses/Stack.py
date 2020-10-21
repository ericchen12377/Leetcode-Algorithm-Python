class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        start = 0
        n = len(s)
        
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if not stack:
                    start = i + 1
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i - start + 1)
                    else:
                        res = max(res, i - stack[-1])
        return res