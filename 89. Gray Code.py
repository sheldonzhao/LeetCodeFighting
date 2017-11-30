'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2
'''
'''
method: iteration
time=O(pow(2,1)+...+pow(2,n))
simplest way：return [(i>>1)^i for i in range(2**n)]
'''


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 0: return []
        if n == 0: return [0]
        if n == 1: return [0, 1]
        res = ['0', '1']
        while n - 1:
            res1 = ['0' + i for i in res]
            res2 = ['1' + i for i in res]
            res = res1 + res2[::-1]
            n -= 1
        res = [int(i, 2) for i in res]
        return res


mySolution = Solution()
re = mySolution.grayCode(3)
print(re)
