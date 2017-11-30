'''
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        stack = []
        result = 0
        left = -1
        for i in range(len(s)):
            if s[i] == '(':
                if left != -1:
                    stack.append(left)
                    left = -1
                else:
                    stack.append(i)
            else:
                if stack:
                    left = stack.pop()
                    result = max(i - left + 1, result)
                else:
                    left = -1
        return result

mySolution = Solution()
s = "()(()"
re = mySolution.longestValidParentheses(s)
print(re)
