class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums)-1
        
        if nums[right] > nums[0]:
            return nums[0]
        
        while left <= right:
            mid = left + (right - left) / 2
            
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[right]


class Solution(object):
    def findMin(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if A[0] <= A[-1]:
            return A[0]
        else:
            low, high = 0, len(A) - 1
            mid = low + (high - low)//2
            while((high - low)>1):
                if (A[mid] > A[high]):
                    low = mid
                else:
                    high = mid
                mid = low + (high - low)//2
        return min(A[low], A[high])
                