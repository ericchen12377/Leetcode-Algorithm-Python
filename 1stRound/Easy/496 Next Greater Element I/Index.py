class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for num1 in findNums:
            index = -1
            for i,nums2 in enumerate(nums):
                if num1 == nums[i]:
                    index = i              #find index of num1 in num2
                    break
            while index < len(nums) and num1 >= nums[index]:        #compare with the next
                index += 1
            if index == len(nums):
                answer.append(-1)
            else:
                answer.append(nums[index])            
        return answer
nums1 = [2,4]
nums2 = [1,2,3,4]
p = Solution()
print(p.nextGreaterElement(nums1,nums2))