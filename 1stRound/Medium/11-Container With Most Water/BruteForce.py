class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 1:
            return 0
        maxarea = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                minheight = min(height[i], height[j])
                width = j - i
                maxarea = max(maxarea, minheight * width)
        return maxarea