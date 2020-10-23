class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        
        i = 0
        n = len(height)
        res = 0
        
        while(i < n):
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                if not stack:
                    continue
                res += (min(height[i], height[stack[-1]]) - height[t]) * (i - stack[-1] - 1)
        return res