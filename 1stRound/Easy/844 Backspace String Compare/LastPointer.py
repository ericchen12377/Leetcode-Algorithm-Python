class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        
        """
        
        pS = len(S) - 1
        pT = len(T) - 1
        while pS >= 0 or pT >= 0:
            if (S[pS] == '#' or T[pT] == '#'):
                if S[pS] == '#':
                    backcount = 2
                    while backcount > 0 :
                        pS -= 1
                        backcount -= 1
                        print([S[pS],pS, backcount])
                        if S[pS] == '#' and pS >= 0:
                            backcount += 2
                elif T[pT] == '#':
                    backcount = 2
                    while backcount > 0:
                        pT -= 1
                        backcount -= 1
                        if T[pT] == '#' and pT >= 0:
                            backcount += 2
            else:
                if S[pS] != T[pT]:
                    return False
                else:
                    pS -= 1
                    pT -= 1
        return True
        