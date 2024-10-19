class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in cnt.items():
            buckets[freq].append(val)
        
        return list(chain(*buckets[::-1]))[:k]
    


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in cnt.items():
            buckets[freq].append(val)
        
        res = []
        for bucket in reversed(buckets):
            for val in bucket:
                res.append(val)
                k -=1
                if k == 0:
                    return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return [val for val, _ in cnt.most_common(k)]