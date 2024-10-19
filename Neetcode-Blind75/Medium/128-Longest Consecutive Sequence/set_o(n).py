class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        if not nums:
            return 0
        unique = set(nums)
        for i in unique:

            if i-1 not in unique:
                current_num = i
                streak = 1
                while current_num+1 in unique:
                    current_num +=1
                    streak+=1
                max_streak = max(streak, max_streak)

        return max_streak
    



    class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        else:
            arr=set()
            for i in nums:
                arr.add(i)
            longest=1
            for i in arr:
                if i-1 not in arr:
                    x=i
                    cnt=1
                    while x+1 in arr:
                        x=x+1
                        cnt=cnt+1
                    longest=max(longest,cnt)
            return longest
