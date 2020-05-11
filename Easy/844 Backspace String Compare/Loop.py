class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        ans_S = ""
        ans_T = ""
        for s in S:
            if s == '#':
                if ans_S:
                    ans_S = ans_S[:-1]
            else:
                ans_S += s
        for t in T:
            if t == '#':
                if ans_T:
                    ans_T = ans_T[:-1]
            else:
                ans_T += t
        return ans_S == ans_T
