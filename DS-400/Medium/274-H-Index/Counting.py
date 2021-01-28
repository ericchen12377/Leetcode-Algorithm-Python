class Solution:
    def hIndex(self, citations):
        n = len(citations)
        # papers[i] is the number of papers with i citations.
        papers = [0] * (n + 1)
        for c in citations:
            # All papers with citations larger than n is count as n.
            papers[min(n, c)] += 1
        i = n
        s = papers[n]  # sum of papers with citations >= i
        while i > s:
            i -= 1
            s += papers[i]
        return i
