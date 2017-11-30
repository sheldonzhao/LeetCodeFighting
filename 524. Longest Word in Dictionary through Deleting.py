'''
Given a string and a string dictionary, find the longest string in the dictionary that can be
formed by deleting some characters of the given string. If there are more than one possible results,
return the longest word with the smallest lexicographical order. If there is no possible result,
return the empty string.
Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]
Output:
"a"
'''


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ans = []
        d = sorted(d, key=len)
        flag = 0
        for i in range(len(d)):
            string = d[-i - 1]
            if self.compare(s, string):
                ans.append(string)
            if ans:
                longest_len = len(ans[0])
                re = all([len(i) == longest_len for i in ans])
                if re is False:
                    flag = 1
            if flag == 1:
                break
        if ans:
            longest_len = len(ans[0])
        else:
            return ''
        bestword = ans[0]
        for i in ans:
            if len(i) == longest_len and i < bestword:
                bestword = i
        return bestword

    def compare(self, s, string):
        index = 0
        len_s = len(string)
        for i in s:
            if index < len_s and i == string[index]:
                index += 1
        return True if index == len_s else False


mySolution = Solution()
s = "bab"
d = ["ba", "ab", "a", "b"]
re = mySolution.findLongestWord(s, d)
print(re)
