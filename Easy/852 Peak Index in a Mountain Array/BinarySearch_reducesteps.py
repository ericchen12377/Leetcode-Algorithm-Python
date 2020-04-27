class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        left, right = 0, N
        while left < right:
            mid = left + (right - left) // 2
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return -1
A = [0,2,1,0]
p = Solution()
print(p.peakIndexInMountainArray(A))