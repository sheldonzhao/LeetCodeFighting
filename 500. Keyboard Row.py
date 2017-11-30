class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        string1 = 'qwertyuiop'
        string2 = 'asdfghjkl'
        string3 = 'zxcvbnm'
        ans = []
        for word in words:
            temp = word.lower()
            count1, count2, count3 = 0, 0, 0
            for letter in temp:
                if letter in string1:
                    count1 += 1
                elif letter in string2:
                    count2 += 1
                else:
                    count3 += 1
            if count1 != 0 and count2 == 0 and count3 == 0 \
                    or count2 != 0 and count1 == 0 and count3 == 0 \
                    or count3 != 0 and count1 == 0 and count2 == 0:
                ans.append(word)
        return ans


mySolution = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
re = mySolution.findWords(words)
print(re)
