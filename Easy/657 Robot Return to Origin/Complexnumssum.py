class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        directs = {'L':-1, 'R':1, 'U':1j, 'D':-1j} # real for axis x and complex for axis y
        return 0 == sum(directs[move] for move in moves)
moves = "UD"
p = Solution()
print(p.judgeCircle(moves))