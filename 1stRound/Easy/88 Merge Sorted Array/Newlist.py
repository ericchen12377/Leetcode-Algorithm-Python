class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums = [n1 for i, n1 in enumerate(nums1) if i < m] + [n2 for i, n2 in enumerate(nums2) if i < n]
        nums.sort()
        for i, num in enumerate(nums):
            nums1[i] = num
nums1 = [1,2,3,0,0,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
p = Solution()
p.merge(nums1,m,nums2,n)
print(nums1)
print(nums2)