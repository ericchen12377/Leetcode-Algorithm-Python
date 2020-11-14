class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return float('inf')
        low = 0
        high = len(nums) - 1
        while low <= high:
            if low == high:
                return nums[low]
            mid = low + (high - low) // 2
            ele = nums[mid]
            if ele > nums[high]:
                low = mid + 1
            elif ele == nums[high]:
                if ele != nums[low]:
                    if nums[mid - 1] > ele:
                        return ele
                    high = mid - 1
                else:
                    return min(self.findMin(nums[ : mid]), self.findMin(nums[mid + 1 : ]))
            else:
                if mid == 0 or nums[mid - 1] > ele:
                    return ele
                high = mid - 1