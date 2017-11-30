'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.
'''


class Solution():
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        len_t = len(t)
        len_s = len(s)
        position_t = 0
        for i in range(len_s):
            re_value = self.resursion(s[i], position_t, len_t, t)
            if re_value == 0:
                return False
            else:
                position_t = re_value[1]

        return True

    def resursion(self, num_s, position_t, len_t, t):
        for i in range(position_t, len_t):
            if num_s == t[i]:
                return [1, i + 1]

        return 0


solution = Solution()
s1 = "abc"
t1 = "ahbgdc"
s2 = "axc"
t2 = "ahbgdc"

print(solution.isSubsequence(s1, t1))
print(solution.isSubsequence(s2, t2))
