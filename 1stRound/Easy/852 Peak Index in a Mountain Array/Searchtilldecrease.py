class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A) - 1):
            if A[i + 1] < A[i]:
                return i
        return -1
A = [0,2,1,0]
p = Solution()
print(p.peakIndexInMountainArray(A))