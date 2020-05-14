class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in range(n - 1):
            prev = res[0]
            count = 1
            ans = ""
            for j in range(1, len(res)):
                cur = res[j]
                if prev != cur:
                    ans = ans + str(count) + str(prev)
                    prev = cur
                    count = 0
                count += 1
            res = ans + str(count) + str(prev)
        return res
