'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        sign = 0
        s = ''
        while i >= 0 or j >= 0:
            if i >= 0:
                sign += int(a[i])
                i -= 1
            if j >= 0:
                sign += int(b[j])
                j -= 1
            s += str(sign % 2)
            sign = sign // 2
        if sign > 0:
            s += '1'
        return s[::-1]


mySolution = Solution()
a = '101111'
b = '10'
re = mySolution.addBinary(a, b)
print(re)
