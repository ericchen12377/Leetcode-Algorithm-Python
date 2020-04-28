import collections
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = collections.Counter(nums1) #create counter dictionary
        count2 = collections.Counter(nums2)
        res = []
        for k, v in count1.items():
            if k in count2:
                res += [k] * min(v, count2[k]) # get the min of two counters for each k
        return res
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
p = Solution()
print(p.intersect(nums1, nums2))