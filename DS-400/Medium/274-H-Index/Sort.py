class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        if len(citations) == 0 or citations == [0]:
            return 0
        citations.sort()
        for i in range(size):
            if citations[i] >= size - i:
                return size - i
        return 0


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)

        for idx, citation in enumerate(citations):

            # find the first index where citation is smaller than or equal to array index
            if idx >= citation:
                return idx

        return len(citations)
