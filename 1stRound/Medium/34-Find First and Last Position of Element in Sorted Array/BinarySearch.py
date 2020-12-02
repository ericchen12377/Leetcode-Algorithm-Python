class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, left, right, target):
            while left <= right:
                mid = (left + right) // 2
                foundval = nums[mid]
                if foundval == target:
                    return mid
                elif foundval < target:
                    left = mid + 1
                elif foundval > target:
                    right = mid - 1
            return -1
        
        if not nums:
            return [-1, -1]
        firstpos = binarySearch(nums, 0, len(nums) - 1, target)
        if firstpos == -1:
            return [-1, -1]
        startpos = firstpos
        endpos = firstpos
        temp1 = 0
        temp2 = 0
        
        while startpos != -1:
            temp1 = startpos
            startpos = binarySearch(nums, 0, startpos-1, target)
        startpos = temp1
        while endpos != -1:
            temp2 = endpos
            endpos = binarySearch(nums, endpos+1, len(nums)-1, target)
        endpos = temp2
        
        return [startpos, endpos]
        