class Solution(object):
    def getPermutation(self, n, k):
        array = range(1, n + 1)
        k = (k % math.factorial(n)) - 1
        permutation = []
        for i in xrange(n - 1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            permutation.append(array.pop(idx))

        return "".join(map(str, permutation))