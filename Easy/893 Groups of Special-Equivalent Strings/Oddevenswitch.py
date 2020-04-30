class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        B = set()
        for a in A:
            B.add(''.join(sorted(a[0::2])) + ''.join(sorted(a[1::2]))) #switch odd and even and keep unchanged
        return len(B)
A = ["abc","acb","bac","bca","cab","cba"]
p = Solution()
print(p.numSpecialEquivGroups(A))