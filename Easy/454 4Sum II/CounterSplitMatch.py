import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # AB = collections.Counter(a + b for a in A for b in B)
        # return sum(AB[-c-d] for c in C for d in D)

        AC = collections.Counter(a + c for a in A for c in C)
        return sum(AC[-b-d] for b in B for d in D)
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
p = Solution()
print(p.fourSumCount(A,B,C,D))