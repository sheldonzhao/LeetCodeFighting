'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return

        len_s = len(s)
        pos = 0
        while pos != len_s:
            re = self.search(s[pos:], wordDict)
            if re == -1:
                return False
            pos += re
        return True

    def search(self, s, wordDict):
        len_s = len(s)
        for i in range(len_s + 1):
            if s[0:i] in wordDict:
                return i
        return -1


mySolution = Solution()
s = "aaaaaaa"
dict = ["aaaa", "aa"]
flag = mySolution.wordBreak(s, dict)
print(flag)
