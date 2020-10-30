class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        print(c)
        nums.clear()
        for i in c:
            if c[i] <= 2:
                for _ in range(c[i]):
                    nums.append(i)
            else:
                for _ in range(2):
                    nums.append(i)
        print(nums)
        