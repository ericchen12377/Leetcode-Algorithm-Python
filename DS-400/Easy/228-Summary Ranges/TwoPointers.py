class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        slow = 0
        fast = 1
        start = 0
        
        res = []
        
        while fast < len(nums):
            if nums[fast] - nums[slow] > 1:
                # check if we append one element
                if start == slow:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start]) + "->" + str(nums[slow]))
                start = fast
                slow = fast
                fast = slow + 1
            else:
                slow += 1
                fast += 1
        
        # append last elements
        if start == slow:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + "->" + str(nums[slow]))
        
        return res
        