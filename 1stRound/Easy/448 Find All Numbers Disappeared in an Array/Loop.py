class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cList = list(range(1, len(nums) + 1))
    	returnList = []
    	for x in nums:
    		cList[x - 1] = 0
    	for x in cList:
    		if x != 0:
    			returnList.append(x)
    	return returnList
p = Solution()
nums = [4,3,2,7,8,2,3,1]
print(p.findDisappearedNumbers(nums))