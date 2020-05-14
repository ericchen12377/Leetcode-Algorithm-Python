class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = [x for x in A if x % 2 == 1] #create list for each odd
        even = [x for x in A if x % 2 == 0] # create list for each even
        res = []
        iseven = True 
        while odd or even:
            if iseven:
                res.append(even.pop())
            else:
                res.append(odd.pop())
            iseven = not iseven
        return res
A = [4,2,5,7]
p = Solution()
print(p.sortArrayByParityII(A))