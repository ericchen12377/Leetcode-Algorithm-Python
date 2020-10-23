class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res =  0
        left = 0
        right = len(height) - 1
        
        while left < right:
            mn = min(height[left], height[right])
            if height[left] == mn:
                left += 1
                while(left < right and height[left] < mn):
                    res += mn - height[left]
                    left += 1
            else:
                right -= 1
                while(left<right and height[right] < mn):
                    res += mn - height[right]
                    right -= 1
        return res