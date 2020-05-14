class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines = 1
        last = 0
        for s in S:
            width = widths[ord(s) - ord('a')] #find width for the letter using ASCII code
            last += width
            if last > 100:
                lines += 1
                last = width
        return [lines, last]

widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10] #width given for each letter
S = "abcdefghijklmnopqrstuvwxyz"
p = Solution()
print(p.numberOfLines(widths,S))