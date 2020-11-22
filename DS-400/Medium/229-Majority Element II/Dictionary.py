class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        res = []
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            elif i in dic.keys():
                dic[i] += 1
            if dic[i] > len(nums) / 3:
                res.append(i)
        return set(res)