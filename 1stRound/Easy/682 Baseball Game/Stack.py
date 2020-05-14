class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valid = []
        for op in ops:
            if op == 'C':
                valid.pop()
            elif op == 'D':
                valid.append(valid[-1] * 2)
            elif op == '+':
                valid.append(valid[-1] + valid[-2])
            else:
                valid.append(int(op))
        return sum(valid)
ops = ["5","2","C","D","+"]
p = Solution()
print(p.calPoints(ops))