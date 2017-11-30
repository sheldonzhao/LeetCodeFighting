'''Given an integer, return a base 7 representation of it as a String.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
'''


class Solution(object):
    def convertTo7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        ans = ''
        if num < 0:
            num = -num
            ans += '-'

        digit = []
        while num:
            digit.append(int(num % 7))
            num //= 7
        digit = digit[::-1]

        for i in digit:
            ans += str(i)
        return ans


mySolution = Solution()
num = 100
re = mySolution.convertTo7(num)
print(re)
