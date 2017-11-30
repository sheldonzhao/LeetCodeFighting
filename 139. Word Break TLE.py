'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''
import time


class Solution(object):
    flag = 0  # if flag =1, return True

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return False

        len_s = len(s)
        for i in range(len_s + 1):
            if self.flag == 1:
                break
            if s[0:i] in wordDict:
                if s[i:] == '':  # 字符串运行完只剩空,成功匹配
                    self.flag = 1
                self.startDFS(s[i:], wordDict)

        if self.flag == 1:
            return True
        else:
            return False

    def startDFS(self, s, wordDict):
        len_s = len(s)
        for i in range(len_s + 1):
            #  让后续无数的startDFS尽快运行完
            if self.flag == 1:
                return
            if s[0:i] in wordDict:
                if s[i:] == '':  # 字符串运行完只剩空,成功匹配
                    self.flag = 1
                    return
                self.startDFS(s[i:], wordDict)


mySolution = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
dict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
start = time.time()
flag = mySolution.wordBreak(s, dict)
end = time.time()

print(flag)
print(end - start)
