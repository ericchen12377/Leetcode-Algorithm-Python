class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        x = str(x)
        N = len(x)
        for i in range(N / 2):
            if x[i] != x[N - 1 - i]:
                return False
        return True
