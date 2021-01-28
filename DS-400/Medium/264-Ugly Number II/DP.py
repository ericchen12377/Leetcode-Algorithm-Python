class Solution:

    # look-up table to speed up query response time
    # it is updated by dynamic programming
    table = []

    def build_look_up_table(self):

        dp = Solution.table

        # base case, minimum ugly number is 1
        dp.append(1)

        # general case, compute next ugly number from previous cases
        idx_2, idx_3, idx_5 = 0, 0, 0

        # maximum n is defined in description
        max_n = 1690

        for _ in range(1, max_n):

            next_2k, next_3k, next_5k = dp[idx_2] * \
                2, dp[idx_3] * 3, dp[idx_5] * 5

            # next ugly number is smallest multiples among 2, 3, 5
            next_ugly_num = min(next_2k, next_3k, next_5k)

            dp.append(next_ugly_num)

            # update index for 2, 3, 5 if needed
            if next_ugly_num == next_2k:
                idx_2 += 1

            if next_ugly_num == next_3k:
                idx_3 += 1

            if next_ugly_num == next_5k:
                idx_5 += 1

        return

    def nthUglyNumber(self, n: int) -> int:

        if not Solution.table:

            # build once, and query for all
            self.build_look_up_table()

        return Solution.table[n-1]
