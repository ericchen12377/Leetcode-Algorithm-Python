import collections
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count_A = collections.Counter(A.split(' '))
        count_B = collections.Counter(B.split(' '))
        words = list((count_A.keys() | count_B.keys()) - (count_A.keys() & count_B.keys())) #create union set
        ans = []
        for word in words:
            if count_A[word] == 1 or count_B[word] == 1: #check if only appear once
                ans.append(word)
        return ans
A = "this apple is sweet"
B = "this apple is sour"
p = Solution()
print(p.uncommonFromSentences(A,B))