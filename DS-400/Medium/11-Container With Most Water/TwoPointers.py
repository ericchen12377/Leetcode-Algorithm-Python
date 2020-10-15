class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            area = max(area, min(height[left], height[right]) * (right - left))
            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1
        
        return area

height = [1, 2, 1]
p = Solution()
print(p.maxArea(height))

