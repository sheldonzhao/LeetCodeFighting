'''

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

'''

import time


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        length = len(words)
        l = []

        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                s = words[i] + words[j]
                len_s = len(s)
                if len_s % 2 == 0:
                    if s[:(len_s // 2)] == s[:(len_s // 2) - 1:-1]:
                        l.append([i, j])
                else:
                    if s[:(len_s // 2)] == s[:(len_s // 2):-1]:
                        l.append([i, j])
        return l


word2 = ["abcd", "dcba", "lls", "s", "sssll"]
mySolution = Solution()
start = time.time()
return_nums = mySolution.palindromePairs(word2)
end = time.time()
# print(end-start)
print(return_nums)
