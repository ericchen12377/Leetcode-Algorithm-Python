class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower = -1 << 31
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
            # print(lower)
            # print(stack)
        return True

[5,2,6,1,3]
-2147483648
[5]
-2147483648
[5, 2]
5
[6]
false