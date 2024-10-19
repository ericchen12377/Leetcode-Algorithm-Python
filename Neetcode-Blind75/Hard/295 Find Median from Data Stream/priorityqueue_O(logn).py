class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # Initialize two heaps: small to store the smaller half as a max heap
        # and large to store the larger half as a min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # If large heap is not empty and the number is greater than the smallest number in large heap,
        # push it to the large heap. Otherwise, push the negation of the number to the small heap.
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # Balance the heaps by adjusting their sizes if necessary
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If sizes of both heaps are equal, return the average of the maximum element in the small heap
        # and the minimum element in the large heap
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0