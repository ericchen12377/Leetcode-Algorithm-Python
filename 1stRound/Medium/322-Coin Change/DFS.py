class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        if amount < coins[-1]:
            return -1

        l = len(coins)
        self.cur = float('inf')
        # current answer(the worst case)

        def dfs(ptr, rem, count):
            '''ptr is the pointer to current index in coins,
               rem denotes remainder. The money left to be made up.
               count denotes current number of coins used.'''
            if not rem:  # remainder is 0, so one branch of dfs is done.
                self.cur = min(self.cur, count)
            else:
                for i in range(ptr, l):
                    # this following if condition is marvelous!
                    if coins[i] <= rem < coins[i] * (self.cur - count):
                        # coins[i] <= rem gaurantees that 'rem' passed to following dfs will be positive
                        # if coins[i] * (self.cur - count) <= rem,
                        # then we know we cannot get better results
                        # just suppose coins[i] = 1, self.cur = 3, rem = 5.
                        # We can see there is no need to do dfs(i, 4, count+1).
                        dfs(i, rem-coins[i], count+1)

        for i in range(l):
            dfs(i, amount, 0)

        return self.cur if self.cur < float('inf') else -1
