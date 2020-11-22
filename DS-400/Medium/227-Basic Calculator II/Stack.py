class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        sign='+'
        num=0
        for i in range(len(s)):
            if 48<=ord(s[i])<=57:
                num=num*10+int(s[i])
            if s[i] in ['+','-','*','/'] or i+1==len(s):
                if sign=='+':
                    stack.append(num)
                elif sign=='*':
                    stack[-1]*=num
                elif sign=='/':
                    stack[-1]=int(stack[-1]/num)
                elif sign=='-':
                    stack.append(-num)
                num=0
                sign=s[i]
        return sum(stack)