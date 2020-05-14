class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        s = s + "P"
        countA = 0
        countL = 0
        for i in range(N):
            if s[i] == "A":
                countA += 1
            if countA > 1:
                return False
            if s[i] == "L":
                countL += 1
                if countL >= 3:
                    return False
            else:
                countL = 0 #reset if not continue
        return True
p = Solution()
s = "PPALLP"
print(p.checkRecord(s))
s = "PPALLL"
print(p.checkRecord(s))