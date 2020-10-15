class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = max(area, min(height[i], height[j]) * (j - i))
        return area

height = [1, 2, 1]
p = Solution()
print(p.maxArea(height))
