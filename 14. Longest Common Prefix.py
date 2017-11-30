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
        common_str = ''
        index = 0
        len_min = min([len(i) for i in strs])
        while index < len_min:
            s = strs[0][index]
            for string in strs:
                if string[index] != s:
                    return common_str
            index += 1
            common_str += s
        return common_str


mySolution = Solution()
strs = ['aa', 'a']
re = mySolution.longestCommonPrefix(strs)
print(re)
