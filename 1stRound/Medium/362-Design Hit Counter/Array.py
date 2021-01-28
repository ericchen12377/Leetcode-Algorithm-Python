class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.arr.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if len(self.arr) == 0:
            return 0
        while self.arr[0] <= timestamp-300:
            self.arr.pop(0)
            if not self.arr:
                break
        return len(self.arr)
