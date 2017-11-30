'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
'''


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        flag_upper = 0
        flag_first_capital = 0
        if not word: return False
        if word[0].isupper():
            for i in range(1, len(word)):
                if word[i].isupper():
                    flag_upper = 1
                if word[i].islower():
                    flag_first_capital = 1
            return True if flag_first_capital * flag_upper == 0 else False

        else:
            for i in word:
                if not i.islower():
                    return False
            return True
