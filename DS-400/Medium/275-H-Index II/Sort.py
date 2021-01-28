class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        if len(citations) == 0 or citations == [0]:
            return 0
        # citations.sort()
        for i in range(size):
            if citations[i] >= size - i:
                return size - i
        return 0
