'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
'''
'''
# important
mindset: backtracking
'''

from copy import deepcopy


class Solution(object):
    def __init__(self):
        self.res = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s: return [[]]
        self.traversal(s, [])
        return self.res

    def traversal(self, s, current):
        if not s:
            self.res.append(current)
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]):
                current_copy = deepcopy(current)
                current_copy.append(s[:i + 1])
                self.traversal(s[i + 1:], current_copy)

    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True


mySolution = Solution()
s = 'aab'
re = mySolution.partition(s)
print(re)
