class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u = d = l = r = 0
        for move in moves:
            if move == 'U':
                u += 1
            elif move == "D":
                d += 1
            elif move == 'L':
                l += 1
            elif move == 'R':
                r += 1
        return u == d and l == r
moves = "UD"
p = Solution()
print(p.judgeCircle(moves))