class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 1:
            return 0
        maxarea = 0
        left = 0
        right = len(height)-1
        
        while left < right:
            width = right - left
            if height[left] <= height[right]:
                maxarea = max(maxarea, height[left] * width)
                left += 1
            elif height[left] > height[right]:
                maxarea = max(maxarea, height[right] * width)
                right -= 1
        return maxarea