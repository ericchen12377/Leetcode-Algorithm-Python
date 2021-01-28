class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        bal = 0
        count = 0
        for s in S:
            if s == '(':
                bal += 1
            elif s == ')':
                bal -= 1
            if bal == -1:
                count += 1
                bal += 1
        return count + bal