import collections
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        count = collections.Counter(moves) #Counter create dictionary
        return count['U'] == count['D'] and count['L'] == count['R']
moves = "UD"
p = Solution()
print(p.judgeCircle(moves))