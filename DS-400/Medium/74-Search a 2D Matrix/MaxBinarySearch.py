class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0 or matrix == [[]]:
            return False
        
        for i in range(m):
            if matrix[i][-1] == target:
                return True
            elif matrix[i][-1] > target:
                return self.BinarySearch(matrix[i], target)
        return False
                
        
       
    def BinarySearch(self, x, target):
        m = len(x)
        if m == 0 or x == []:
            return False
        left, right = 0, m - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = x[pivot_idx]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False