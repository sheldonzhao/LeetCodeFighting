'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
'''
#important
amazing algorithm
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0] * (len(num1) + len(num2))
        for i, digit1 in enumerate(reversed(num1)):
            for j, digit2 in enumerate(reversed(num2)):
                product[i + j] += (ord(digit1) - ord('0')) * (ord(digit2) - ord('0'))
                product[i + j + 1] += product[i + j] // 10
                product[i + j] %= 10
        print(product)
        return ''.join(map(str, product[::-1])).lstrip('0') or '0'


mySolution = Solution()
num1 = '0'
num2 = '0'
re = mySolution.multiply(num1, num2)
print(re)
