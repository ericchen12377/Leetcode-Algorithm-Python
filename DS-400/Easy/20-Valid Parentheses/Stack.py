class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return stack == []




s = "()[]"
p = Solution()
print(p.isValid(s))
