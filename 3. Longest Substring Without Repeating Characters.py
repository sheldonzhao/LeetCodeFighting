'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ret = []
        len_s = len(s)
        l = []
        for index in range(len_s):
            if s[index] not in l:
                l.append(s[index])
            else:
                ret.append(len(l))
                # slide window
                while s[index] in l:
                    l.pop(0)
                l.append(s[index])

        return max(ret) if ret and max(ret) > len(l) else len(l)


mySolution = Solution()
s = "afdfasdfadsfjldafjlq0wertyuiosasdfgthjukzxcfvgbhnm"
re = mySolution.lengthOfLongestSubstring(s)
print(re)
