'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution(object):
    def __init__(self):
        self.ans = []
        self.pair = ''

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return ['']
        root = '('
        self.traversal(root, n, 0, 0)
        return self.ans

    def traversal(self, root, n, count_left_bracket, count_right_bracket):
        self.pair += root
        if root == '(':
            count_left_bracket += 1
        else:
            count_right_bracket += 1
        if count_left_bracket == n and count_right_bracket == n:
            self.ans.append(self.pair)

        if count_left_bracket != n:
            self.traversal('(', n, count_left_bracket, count_right_bracket)
        if count_left_bracket > count_right_bracket:
            self.traversal(')', n, count_left_bracket, count_right_bracket)
        self.pair = self.pair[0:len(self.pair) - 1]


mySolution = Solution()
n =3
ret = mySolution.generateParenthesis(n)
print(ret)
