class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lower = -1 << 31
        i = 0
        for x in preorder:
            if x < lower:
                return False
            while i > 0 and x > preorder[i - 1]:
                lower = preorder[i - 1]
                i -= 1
            preorder[i] = x
            i += 1
            # print(preorder)
        return True