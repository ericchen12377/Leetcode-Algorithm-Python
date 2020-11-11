class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        stack = [(0, [])]
        res = []
        while stack:
            start, partition = stack.pop()
            rest = s[start:]
            if rest == rest[::-1]:
                res.append(partition + [rest])
            
            substr = ''
            for i in range(start, n - 1):
                substr += s[i]
                if substr == substr[::-1]:
                    stack.append((i + 1, partition + [substr]))
        
        return res