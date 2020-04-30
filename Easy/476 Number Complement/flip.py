class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_num = bin(num)[2:] #remove "0b"
        bin_ans = map(lambda x: '0' if x == '1' else '1', bin_num) #flip 0 and 1
        return int(''.join(bin_ans), 2) #convert binary in int
num = 5
p = Solution()
print(p.findComplement(num))