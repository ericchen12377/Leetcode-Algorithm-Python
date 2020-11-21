class Solution:
    def calculate(self, s: str) -> int:
        ## RC ##
        ## APPROACH : 2 STACKS ##
        ## SIMILAR TO LEETCODE 772. BASIC CALCULATOR III ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(N) ##
		
        def operation(op, second, first):
            if op == "+":
                return first + second
            elif op == "-":
                return first - second
            elif op == "*":
                return first * second
            elif op == "/":  # integer division
                return first // second
        
        def precedence(current_op, op_from_ops):
            if( op_from_ops == "(" or op_from_ops == ")" ):
                return False
            if(current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
                return False
            return True     # when curr = "+", top of ops = "*" or "/"
        
        if not s: return 0
        N = len(s)
        nums = [] if(s[0] !='-') else [0]                                       # edge case -1 + 2/3
        ops = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = c
                while i < N - 1 and s[i + 1].isdigit():                    # more than 1 digit numbers
                    num += s[i + 1]
                    i += 1
                nums.append(int(num))
            elif c == "(":
                ops.append(c)
                if( i+1 < N and s[i+1] == '-'): 
                    nums.append(0)                                              # "1 - (-7)" edge case.
            elif c == ")":
                while ops[-1] != "(":                                           # do the math when we encounter a ')' until '('
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()                                                       # watch out, popping open brace '('
            elif c in ["+", "-", "*", "/"]:
                while len(ops) != 0 and precedence(c, ops[-1]):                 # check for precedence order and make calculations, APPEND RESULT TO NUMS STACK EVERY TIME.
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))   
                ops.append(c)                                                   # append to operators stack
            i += 1                                                              # basic while loop increment
        
        while len(ops) > 0:                                                     # finally we perform calculations till stack is empty.
            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
            
        return nums.pop()