class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums_smaller_count = 0

        for i, n in enumerate(nums[:-2]):
            pointer1, pointer2 = i+1, len(nums)-1
            while pointer1 < pointer2:
                num1, num2 = nums[pointer1], nums[pointer2]
                three_sum = n + num1 + num2
                if three_sum < target:
                    nums_smaller_count += pointer2-pointer1
                    pointer1 += 1
                else:
                    pointer2 -= 1

        return nums_smaller_count
