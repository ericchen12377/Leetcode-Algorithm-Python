class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        Total = 0
        
        for i in range(len(height)):
            maxL = 0
            maxR = 0
            left = i
            right = i
            while left >= 0:
                if height[left] > maxL:
                    maxL = height[left]
                    
                left -= 1
            while right < len(height):
                if height[right] > maxR:
                    maxR = height[right]
                right += 1
            Total += max(0, min(maxL, maxR) - height[i])
        return Total
            