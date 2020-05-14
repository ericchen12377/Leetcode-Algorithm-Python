class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bitmap = [[-1] * 1000 for _ in range(1001)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        row, col = key // 1000, key % 1000
        self.bitmap[row][col] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        row, col = key // 1000, key % 1000
        return self.bitmap[row][col]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        row, col = key // 1000, key % 1000
        self.bitmap[row][col] = -1


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
key = 1
value = 1
obj.put(key,value)
param_1 = obj.get(key)
print(param_1)
obj.remove(key)
param_2 = obj.get(key)
print(param_2)