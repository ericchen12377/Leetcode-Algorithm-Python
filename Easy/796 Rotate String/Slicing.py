class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B == "":
            return True
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False
p = Solution()
A = 'abcde'
B = 'cdeab'
print(p.rotateString(A,B))
A = 'abcde'
B = 'abced'
print(p.rotateString(A,B))