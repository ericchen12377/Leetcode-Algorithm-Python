class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key = lambda x : x % 2) #sort A first and put evens in front and odds in end
        N = len(A)
        res = []
        for i in range(N // 2):  #pick one even from front and one odd from end
            res.append(A[i])
            res.append(A[N - 1 - i])
        return res
A = [4,2,5,7]
p = Solution()
print(p.sortArrayByParityII(A))