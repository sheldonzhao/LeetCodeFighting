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
        # align a with b
        len_max = max(len(a), len(b))
        len_min = min(len(a), len(b))
        if len(a) > len(b):
            s = '0' * (len_max - len_min)
            b = s + b
            a, b = '0' + a, '0' + b
        elif len(a) < len(b):
            s = '0' * (len_max - len_min)
            a = s + a
            a, b = '0' + a, '0' + b
        else:
            a, b = '0' + a, '0' + b
        #  if a[i]+b[i] == 2, carry=1
        carry = 0
        add = []
        for i in range(len(a)):
            value = int(a[-i - 1]) + int(b[-i - 1])
            if carry == 0:
                if value == 2:
                    carry = 1
                    add.append(0)
                else:
                    add.append(value)
            else:
                if value == 2:
                    carry = 1
                    add.append(1)
                elif value + 1 == 2:
                    add.append(0)
                    carry = 1
                else:
                    add.append(1)
                    carry = 0
        s = ''
        for i in range(len(add)):
            s += str(add[-i - 1])
        # prevent case '0' and '0'
        if s == '00': return '0'
        return s.lstrip('0')


mySolution = Solution()
a = '0'
b = '0'
re = mySolution.addBinary(a, b)
print(re)
