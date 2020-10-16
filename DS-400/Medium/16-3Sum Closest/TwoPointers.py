class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        #sort the list
        nums.sort()
        sumres = []
        res = 0
        dis = 1e10

        i = 0
        while(i < len(nums)-1):
            print(nums[i])
            low = i + 1
            high = len(nums) - 1
            while(low < high):
                sum = nums[i]+nums[low]+nums[high]
                if(abs(sum - target) < abs(dis)):
                    res = nums[i]+nums[low]+nums[high]
                    dis = nums[i]+nums[low]+nums[high] - target
                elif sum < target:
                    low += 1
                else:
                    high -= 1
            if dis == 0:
                break
            i += 1
        return res


nums = [1,2,4,8,16,32,64,128]
target = 82
p = Solution()
print(p.threeSumClosest(nums, target))