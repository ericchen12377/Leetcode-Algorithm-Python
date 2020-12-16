class Solution:
    def __init__(self):
        self.mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        self.all_self_nums = ["0", "1", "8"]
        self.all_nums = ["0", "1", "6", "8", "9"]
        self.all_non_zero_nums = ["1", "6", "8", "9"]
    
    def _permutate(self, base_nums: List[str], nums: List[str]) -> List[str]:
        ret = []
        for bn in base_nums:
            for n in nums:
                ret.append(n + bn + self.mapping[n])
        return ret
    
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return self.all_self_nums
        else:
            if n % 2 == 1:
                start_strings = self.all_self_nums
                for _ in range(n // 2 - 1):
                    start_strings = self._permutate(start_strings, self.all_nums)
                start_strings = self._permutate(start_strings, self.all_non_zero_nums)
            else:
                start_strings = [""]
                for _ in range(n // 2 - 1):
                    start_strings = self._permutate(start_strings, self.all_nums)
                start_strings = self._permutate(start_strings, self.all_non_zero_nums)
            return start_strings