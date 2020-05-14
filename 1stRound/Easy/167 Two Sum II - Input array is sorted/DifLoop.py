class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        N = len(numbers)
        while N > 1:
            dif = target - numbers[N-1]
            if dif > 0:
                if dif in numbers[:N-2]:
                    return [numbers.index(dif)+1,N]
                else:
                    N = N - 1
            else:
                N = N - 1
        return[0,0]

numbers = [2,11,7,15]
target = 9
p = Solution()
print(p.twoSum(numbers,target))