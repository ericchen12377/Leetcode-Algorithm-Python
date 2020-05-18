class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        print(A)
        N = len(A)
        if N < 3: return False
        i = 0
        while i < N - 1 and A[i + 1] > A[i]:
            i += 1
        if i == 0 or i == N - 1: return False
        while i < N - 1 and A[i] > A[i + 1]:
            i += 1
        return i == N - 1
