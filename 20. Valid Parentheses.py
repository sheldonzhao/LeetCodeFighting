'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            elif i == '(':
                stack.append(')')
            elif stack == [] or i != stack.pop():
                return False
        return stack == []


s = Solution()
res = s.isValid(']')
print(res)
