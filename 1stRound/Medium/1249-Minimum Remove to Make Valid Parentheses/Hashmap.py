class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return True
        res = list(s)
        print(res)
        stack = []
        for i in range(len(res)):
            if res[i] == '(':
                stack.append(i)
            elif res[i] == ')' and stack:
                    stack.pop()
            elif res[i] == ')':
                res[i] = ""
        while stack:
            idx = stack.pop()
            res[idx] = ""
        return "".join(res)