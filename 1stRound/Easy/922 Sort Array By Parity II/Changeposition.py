class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        res = [0] * N
        even, odd = 0, 1
        for a in A:
            if a % 2 == 1:
                res[odd] = a #put odd in odd position
                odd += 2
            else:
                res[even] = a #put even in even position
                even += 2
        return res
A = [4,2,5,7]
p = Solution()
print(p.sortArrayByParityII(A))