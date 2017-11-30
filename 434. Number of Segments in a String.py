'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
Input: "Hello, my name is John"
Output: 5
'''


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        flag = 0
        count = 0
        for i in s:
            if not i == ' ':
                if flag == 0:
                    count += 1
                flag = 1
            else:
                flag = 0
        return count


mySolution = Solution()
s = 'Hello, my name is John'
s2 = "love live! mu'sic forever"
print(mySolution.countSegments(s2))
