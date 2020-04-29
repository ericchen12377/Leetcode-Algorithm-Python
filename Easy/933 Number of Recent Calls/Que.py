import collections
class RecentCounter:

    def __init__(self):
        self.que = collections.deque() #list-like container with fast appends and pops on either end

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.que and self.que[0] < t - 3000:
            self.que.popleft() # pop any before t
        self.que.append(t) # add t
        return len(self.que) #check the rest length
# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))