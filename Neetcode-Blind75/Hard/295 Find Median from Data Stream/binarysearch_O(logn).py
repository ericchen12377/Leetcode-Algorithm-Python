class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
    
        beg=0
        end=len(self.arr)
        while beg<end:
            mid=(end+beg)//2
            
            if self.arr[mid]>num:
                end=mid
            else:
                beg=mid+1
        
        self.arr.insert(beg,num)


    def findMedian(self) -> float:
        n=len(self.arr)
        if n%2==1:
            return self.arr[n//2]
        else:
            return (self.arr[n//2-1]+self.arr[n//2])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()