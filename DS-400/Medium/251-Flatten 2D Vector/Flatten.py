class Vector2D:

    def __init__(self, v: List[List[int]]):
        

        self.final = []

        for l in v:
            self.final+=l

        self.final.reverse()

    def next(self) -> int:
        return self.final.pop()
        

    def hasNext(self) -> bool:
        return self.final
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()