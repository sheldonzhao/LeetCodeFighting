'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for i in path.split('/'):
            if i == '..':
                if stack:
                    stack.pop()
            else:
                if not (i == '..' or i == '.' or i == ''):
                    stack.append(str(i))
        return '/'+'/'.join(stack)


mySolution = Solution()
path = "/"
re = mySolution.simplifyPath(path)
print(re)
