import statistics
class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        return statistics.median(self.arr)