class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums):
            return len(set(nums)) < len(nums)
        setNum = set()
        for i,num in enumerate(nums):
            if i > k:
                setNum.remove( nums[i-k-1])
            len1 = len(setNum)
            setNum.add(num)
            if len1 == len(setNum):
                return True
        return False