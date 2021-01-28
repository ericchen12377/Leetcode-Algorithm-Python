class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        size = len(time)
        for i in range(size):
            for j in range(i+1, size):
                    count += (time[i] + time[j]) % 60 == 0
        return count
