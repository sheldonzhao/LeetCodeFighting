'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens: return 0
        stack = []
        operation = {"+": lambda x, y: y + x, "-": lambda x, y: y - x, '*': lambda x, y: y * x, '/':
            lambda x, y: y / x}
        for i in tokens:
            if i in operation:
                stack.append(int(operation[i](stack.pop(), stack.pop())))
            else:
                stack.append(float(i))
        return int(stack[0])


mySolution = Solution()
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
re = mySolution.evalRPN(tokens)
print(re)
