class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(numbers)
        left, right = 0, N - 1
        while left < right:
            cursum = numbers[left] + numbers[right]
            if cursum == target:
                return [left + 1, right + 1]
            elif cursum < target:
                left += 1
            else:
                right -= 1
        return [0, 0]
numbers = [2,11,7,15]
target = 9
p = Solution()
print(p.twoSum(numbers,target))