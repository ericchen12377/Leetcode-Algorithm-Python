class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines, row = 1, 0
        lendict = {c : widths[i] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")} #save width in dictionary for each letter
        N = len(S)
        for s in S:
            if row + lendict[s] > 100:
                row = lendict[s]
                lines += 1
            else:
                row += lendict[s]
        return lines, row
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10] #width given for each letter
S = "abcdefghijklmnopqrstuvwxyz"
p = Solution()
print(p.numberOfLines(widths,S))