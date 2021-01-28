class Solution:
    def isUgly(self, num: int) -> bool:
        while num > 0:
            if num % 2 == 0:
                num = num//2
            elif num % 3 == 0:
                num = num//3
            elif num % 5 == 0:
                num = num//5
            elif num == 1:
                return True
            else:
                return False
        return False
