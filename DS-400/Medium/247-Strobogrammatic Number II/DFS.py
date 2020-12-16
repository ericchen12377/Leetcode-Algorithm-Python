class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.mapping = {"0": "0", "1": "1", "6": "9", "9": "6", "8": "8"}
        self.res = []
        if n % 2:
            for i in ["0", "8", "1"]:
                self.dfs(str(i), n - 1)
        else:
            self.dfs("", n)
        return self.res
        
    def dfs(self, num, n):
        if n == 0:
            self.res.append(num)
            return
            
        for number in self.mapping:
            if n == 2 and number != "0":
                self.dfs(number + num + self.mapping[number], n - 2)
            elif n > 2:
                self.dfs(number + num + self.mapping[number], n - 2)