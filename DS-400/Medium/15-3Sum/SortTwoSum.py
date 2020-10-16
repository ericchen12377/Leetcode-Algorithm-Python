class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sort the list
        nums.sort()
        res = []

        i = 0
        while(i < len(nums)-1):
            if nums[i] > 0:
                break
            elif i == 0 or (nums[i] != nums[i-1]):
                low = i + 1
                high = len(nums) - 1
                target = 0 - nums[i]
                while(low < high):
                    if nums[low] + nums[high] > target:
                        high -= 1
                    elif nums[low] + nums[high] < target:
                        low += 1
                    elif nums[low] + nums[high] == target:
                        res.append([nums[i], nums[low], nums[high]])
                        high -= 1
                        low += 1
                        while(low < high and nums[low] == nums[low - 1]):
                            low += 1
            i += 1
        return res





nums = [-1,0,1,2,-1,-4]
p = Solution()
print(p.threeSum(nums))