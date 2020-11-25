class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)
        self.s2 = self.s1[::-1]

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        i = self.s2.pop()
        self.s1 = self.s2[::-1]
        return i

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if (len(self.s1)==0):
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()