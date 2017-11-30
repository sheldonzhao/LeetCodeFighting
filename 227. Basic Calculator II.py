'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
'''


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        l = []
        len_s = len(s)
        flag = 0
        for i in range(len_s):
            if s[i].isdigit():
                if flag == 1:
                    l[-1] += s[i]
                else:
                    l.append(s[i])
                    flag = 1
            elif s[i] in '+-*/':
                l.append(s[i])
                flag = 0
        while '*' in l or '/' in l:
            index=None
            for i in range(len(l)):
                if l[i] == '*':
                    index=i
                    break
                elif l[i] == '/':
                    index=i
                    break
            if l[index] == '*':
                l[index] = int(l[index - 1]) * int(l[index + 1])
            else:
                l[index] = int(l[index - 1]) // int(l[index + 1])
            l.pop(index - 1)
            l.pop(index)
        value = int(l[0])
        for i in range(len(l)):
            if l[i] == '+':
                value += int(l[i + 1])
            if l[i] == '-':
                value -= int(l[i + 1])
        return value


mySolution = Solution()
s = "      30/3*4-10+5"
re = mySolution.calculate(s)
print(re)
