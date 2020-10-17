class Solution:
    def generateParenthesis(self, n: int):
        base_case = set([ "()" ])
        for i in range(1, n):
            base_case = self.slide_sert(base_case)
        return base_case

    
    def slide_sert(self, paren_set):
        newly_injected_parens = set()
        for paren in paren_set: # for each paren string
            for injection_index in range(len(paren)): # go through each possible injection site
                newly_injected_parens.add(paren[:injection_index] + '()' + paren[injection_index:])

        return newly_injected_parens

n = 3
p = Solution()
print(p.generateParenthesis(n))


# base_case = set([ "()" ])
# def slide_sert(paren_set):
#         newly_injected_parens = set()
#         for paren in paren_set: # for each paren string
#             print(paren)
#             for injection_index in range(len(paren)): # go through each possible injection site
#                 print(paren[:injection_index])
#                 print(paren[injection_index:])
#                 newly_injected_parens.add(paren[:injection_index] + '()' + paren[injection_index:])
#                 print(newly_injected_parens)
# slide_sert(base_case)