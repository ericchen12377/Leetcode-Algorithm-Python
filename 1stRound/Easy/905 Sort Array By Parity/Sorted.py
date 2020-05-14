class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(A, key = lambda x : x % 2)

input = [3,1,2,4]
p = Solution()
print(p.sortArrayByParity(input))