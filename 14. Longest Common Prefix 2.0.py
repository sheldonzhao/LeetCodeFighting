'''
Write a function to find the longest common prefix string amongst an array of strings.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        len_min = min([len(i) for i in strs])
        start, end = 0, len_min - 1
        while start <= end:
            mid = (start + end) // 2
            if self.binary(strs, start, mid):
                start = mid + 1
            else:
                end = mid - 1
        return strs[0][0:(start + end) // 2 + 1]

    def binary(self, strs, start, end):
        s = strs[0][start:end + 1]
        for string in strs:
            if string[start:end + 1] != s:
                return False
        return True


mySolution = Solution()
strs = ['1234', '1235']
re = mySolution.longestCommonPrefix(strs)
print(re)
