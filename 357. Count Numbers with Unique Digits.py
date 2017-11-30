'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
'''


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10

        count = 10
        for i in range(1, n):
            sub_count = 9
            for j in range(i):
                sub_count *= (9 - j)
            count += sub_count

        return count


mySolution = Solution()
num = 3
print(mySolution.countNumbersWithUniqueDigits(num))
