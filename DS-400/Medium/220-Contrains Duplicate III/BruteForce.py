class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(nums) == len(set(nums)):
            return False
        
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if i == j:
                    continue
                elif abs(nums[j]-nums[i]) <= t and abs(j-i) <= k:
                    return True

        return False