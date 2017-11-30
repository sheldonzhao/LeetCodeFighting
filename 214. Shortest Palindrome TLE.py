'''
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:
Given "aacecaaa", return "aaacecaaa".
Given "abcd", return "dcbabcd".
'''
'''
method: brute force
'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        for i in range(len_s):
            if self.judge(s[:len_s - i], len_s - i):
                return s[:len_s - i - 1:-1] + s

    def judge(self, s, len_s):
        if s[:len_s // 2] == s[:(len_s - 1) // 2:-1]:
            return True


mySolution = Solution()
s1 = 'aca'
s2 = 'abcd'
s3 = 'aac'
s4 = '   '
re = mySolution.shortestPalindrome(s3)
print(re)
