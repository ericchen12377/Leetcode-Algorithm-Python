class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        
        """
        sums=[0]
        ss=0
        for i in nums:
            ss+=i
            sums.append(ss)
        ans=[]    
        for i in range(len(nums)):
            left=i
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if sums[mid+1]-sums[i]>=s:
                    ans.append(mid-i)
                    right=mid-1
                else:
                    left=mid+1
        try:
            return min(ans)+1
        except:
            return 0

        