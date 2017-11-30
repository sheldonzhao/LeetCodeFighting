class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        '''
        simplest code
        return bin(x^y).count('1')
        '''
        if x is None or y is None:
            return

        bin_x = bin(x).lstrip('0b')
        bin_y = bin(y).lstrip('0b')
        if len(bin_x) == len(bin_y):
            count = self.cal_diff(bin_x, bin_y)

        if len(bin_x) > len(bin_y):
            for i in range(len(bin_x) - len(bin_y)):
                bin_y = '0' + bin_y
            count = self.cal_diff(bin_x, bin_y)

        if len(bin_x) < len(bin_y):
            for i in range(len(bin_y) - len(bin_x)):
                bin_x = '0' + bin_x
            count = self.cal_diff(bin_x, bin_y)

        return count

    def cal_diff(self, x, y):
        len_x = len(x)
        count = 0
        for i in range(len_x):
            if x[i] != y[i]:
                count += 1
        return count


mySolution = Solution()
count = mySolution.hammingDistance(3, 52)
print(count)
