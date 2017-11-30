'''
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))


mySolution = Solution()
s = "the sky is blue"
s2 = ' '
s3 = '1 '
s4 = "   a   b "
re = mySolution.reverseWords(s3)
print(re)
