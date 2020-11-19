class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        numDict = {}
        for index, num in enumerate(nums):
            if len(numDict) > 2*t:
                for i in range(num-t, num+t+1):
                    if i in numDict and index-numDict[i] <= k:
                            return True
            else:
                for i in numDict:
                    if abs(num-i) <= t and index-numDict[i] <= k:
                        return True
            numDict[num] = index
        return False