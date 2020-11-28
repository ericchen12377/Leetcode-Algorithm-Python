class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        Total = 0
        left, right = 0, len(height) - 1
        maxL = 0
        maxR = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] > maxL:
                    maxL = height[left]
                else:
                    Total += maxL - height[left]
                left += 1
            else:
                if height[right] > maxR:
                    maxR = height[right]
                else:
                    Total += maxR - height[right]
                right -= 1
        return Total
            