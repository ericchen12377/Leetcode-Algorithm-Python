class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd, even = 0, 0
        res = True
        seen = {}
        for l in s:
            if l not in seen:
                seen[l] = 1
            else:
                seen[l] += 1
        countOne = 0
        for i in seen:
            if seen[i] == 1:
                countOne += 1
            elif seen[i] % 2 == 0:
                continue
            elif seen[i] % 2 == 1:
                countOne += 1
        return True if countOne <= 1 else False
