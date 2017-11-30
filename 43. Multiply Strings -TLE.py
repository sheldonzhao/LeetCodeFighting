'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        layer_sum = []
        for i in range(len(num2)):
            carry = 0
            str_sum = ''
            num2_digit = int(num2[-i - 1])
            flag = 0
            for j in range(len(num1)):
                num1_digit = int(num1[-j - 1])
                multiply = num1_digit * num2_digit
                # the multiply of two nums >= 10
                if multiply >= 10:
                    reminder = multiply % 10
                    if carry + reminder < 10:
                        str_sum = str(carry + reminder) + str_sum
                    else:
                        # if flag = 1, carry needs to add 1 in the end
                        flag = 1
                        str_sum = str((carry + reminder) % 10) + str_sum
                # the multiply of two nums < 10
                else:
                    if carry + multiply < 10:
                        str_sum = str(carry + multiply) + str_sum
                    else:
                        carry = 1
                        str_sum = str((carry + multiply) % 10) + str_sum
                if flag == 0:
                    carry = multiply // 10
                else:
                    carry = multiply // 10 + 1
                    flag = 0
            if carry > 0:
                str_sum = str(carry) + str_sum
            layer_sum.append(str_sum)
        print(layer_sum)
        count = 1
        for i in range(len(layer_sum)):
            layer_sum[i] = int(layer_sum[i]) * count
            count *= 10
        sum_value=0
        for i in layer_sum:
            sum_value+=i
        return str(sum_value)


mySolution = Solution()
num1 = '98765'
num2 = '12345'
re=mySolution.multiply(num1, num2)
print(re)