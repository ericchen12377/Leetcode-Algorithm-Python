class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for s in str:
            if ord(s) >= ord('A') and ord(s) <= ord('Z'): # whether in the range 65 ~ 90
                res += chr(ord(s) - ord('A') + ord('a')) #  ord("A")65, ord("a")97
            else:
                res += s
        return res

input = "ABCdefG"
p = Solution()
print(p.toLowerCase(input))
