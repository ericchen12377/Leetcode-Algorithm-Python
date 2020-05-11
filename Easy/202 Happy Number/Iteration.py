class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited: #avoid loop non-stop
            visited.add(n)
            nx = 0
            while n != 0:
                nx += (n % 10) ** 2
                n //= 10
            if nx == 1:
                return True
            n = nx
        return False
