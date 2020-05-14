class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stackS, stackT = [], []
        for s in S:
            if s != "#":
                stackS.append(s)
            elif stackS:
                stackS.pop()
        for t in T:
            if t != "#":
                stackT.append(t)
            elif stackT:
                stackT.pop()
        return stackS == stackT
