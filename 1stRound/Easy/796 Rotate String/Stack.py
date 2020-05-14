class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        stack = list(A)
        tmp = []
        if A == B == "":
            return True
        i = 1
        while i <= len(stack):
            tmp = list(stack.pop())
            tmp.extend(stack)
            if ''.join(tmp) == B:
                return True
            stack = tmp
            i += 1
        return False
p = Solution()
A = 'abcde'
B = 'cdeab'
print(p.rotateString(A,B))
A = 'abcde'
B = 'abced'
print(p.rotateString(A,B))