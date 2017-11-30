'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
'''
method: when meeting operator'+-*/', pop two numbers from stack
learning point: 6 / -11 = -1 int( 6.0 / 11 ) = 0 int(float(6) / 11) = 0
'''


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens: return 0
        stack = []
        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isnumeric():
                stack.append(tokens[i])
            elif tokens[i] in '+-*/':
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+':
                    num = int(b) + int(a)
                if tokens[i] == '-':
                    num = int(b) - int(a)
                if tokens[i] == '*':
                    num = int(b) * int(a)
                if tokens[i] == '/':
                    num = float(b) / int(a)
                stack.append(num)
        return int(stack[0])


mySolution = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
re = mySolution.evalRPN(tokens)
print(re)
