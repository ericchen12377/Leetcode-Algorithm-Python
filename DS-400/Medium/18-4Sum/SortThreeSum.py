class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

         #sort the list
        nums.sort()
        res = []

        i = 0
        n = len(nums)
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j  in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                low = j + 1
                high = n - 1
                while(low < high):
                    sum = nums[i] + nums[j] + nums[low] + nums[high]
                    if sum < target:
                        low += 1
                    elif sum > target:
                        high -= 1
                    else:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        while(low < high and nums[low] == nums[low + 1]):
                            low += 1
                        while(low < high and nums[high] == nums[high - 1]):
                            high -= 1
                        low += 1
                        high -= 1
        return res


nums = [1,0,-1,0,-2,2]
target = 0
p = Solution()
print(p.fourSum(nums, target))