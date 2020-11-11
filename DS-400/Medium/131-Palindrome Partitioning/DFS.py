class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def dfs(currList, k):
            if k == len(s):
                ans.append(currList)
                return

            for i in range(k, len(s)):
                tmpStr = s[k:i + 1]
                if tmpStr == tmpStr[::-1]:
                    dfs(currList + [tmpStr], i + 1)

        dfs([], 0)
        return ans