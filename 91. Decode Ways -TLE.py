'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
The number of ways decoding "12" is 2.
'''
'''
Method: DFS
Time: O(2**n) Space: O(k)
'''


class Solution(object):
    def __init__(self):
        self.ans = 0

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        letter, key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1
        hash_map = {}
        for i in letter:
            hash_map[str(key)] = i
            key += 1
        pos = 0
        len_s = len(s)
        self.DFS(s, pos, len_s, hash_map)
        return self.ans

    def DFS(self, s, pos, len_s, hash_map):
        if pos >= len_s:
            self.ans += 1
            return
        if s[pos] in hash_map:
                self.DFS(s, pos + 1, len_s, hash_map)
        if pos + 1 < len_s and s[pos] + s[pos + 1] in hash_map:
                self.DFS(s, pos + 2, len_s, hash_map)


mySolution = Solution()
s = '123'
re = mySolution.numDecodings(s)
print(re)
