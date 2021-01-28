class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        max_col = 0
        for i in range(len(nums)):
            max_col = max(max_col, len(nums[i]))
        for i in range(len(nums)):
            if len(nums[i]) < max_col:
                nums[i] += [0] * (max_col - len(nums[i]))
        print(nums)
        d = {}
        # loop through matrix
        for col in range(max_col):
            for row in range(len(nums)):
                                # if no entry in dictionary for sum of indices aka the diagonal, create one
                if nums[row][col] != 0:
                    if col + row not in d:
                        d[col+row] = [nums[row][col]]
                    else:
                                    # If you've already passed over this diagonal, keep adding elements to it!
                        d[col+row].append(nums[row][col])
                    # we're done with the pass, let's build our answer array
        print(d)
        ans = []
        # look at the diagonal and each diagonal's elements
        for entry in d.items():
            [ans.append(x) for x in entry[1]]
        return ans
