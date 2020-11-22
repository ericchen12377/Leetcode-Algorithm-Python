class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        
        start = None        
        for i, n in enumerate(nums):
            if start is None:
                start = n
            if i == len(nums) - 1 or n < nums[i + 1] - 1:
                ranges.append(str(start) + "->" + str(n) if start != n else str(n))                
                start = None
            
        return ranges


class Solution:
    def summaryRanges(self, lst: List[int]) -> List[str]:
        res=[]
        for i in lst:
            if i-1 not in lst:
                y=i+1
                while y in lst:
                    y+=1
                if i!=y-1:
                    res.append(str(i)+"->"+str(y-1))
                else:
                    res.append(str(i))
        return res