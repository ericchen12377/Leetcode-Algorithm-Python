class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounter = {}
        topK = []

        if len(nums) == k and len(set(nums)) != k:
            return nums
        elif len(set(nums)) == k:
            return list(set(nums))
        else:
            for x in nums:
                if x not in numCounter.keys():
                    numCounter[x] = 1
                else:
                    numCounter[x] += 1

            counts = list(numCounter.values())
            counts.sort(reverse=True)

            counts = counts[0:k]


            for x,y in numCounter.items():
                if y in counts:
                    topK.append(x)

        return topK