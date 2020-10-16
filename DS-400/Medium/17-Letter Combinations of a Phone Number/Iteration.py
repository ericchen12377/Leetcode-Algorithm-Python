class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dicts = {'1':[''],
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        def combine(pres,dicts,digit):
            """
            :type pres:List[str], dicts: dictionary, digits: str
            :rtype: List[str]
            """
            letL=[]
            for pre in pres:
                for letter in dicts[digit]:
                    letL.append(pre+letter)
            return letL
            
        if digits=='':
            return []
            
        lets=['']
        for digit in digits:
            lets=combine(lets,dicts,digit)
        return lets



digits = "23"
p = Solution()
print(p.letterCombinations(digits))