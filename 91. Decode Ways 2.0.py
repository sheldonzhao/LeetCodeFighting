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
# important
type: 斐波那契数列变种
Method: F(n)=F(n-1)+F(n-2)
'''
'''
for (int i = n - 2; i >= 0; i--)
            if (s.charAt(i) == '0') continue;
            else memo[i] = (Integer.parseInt(s.substring(i,i+2))<=26) ? memo[i+1]+memo[i+2] : memo[i+1];
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s == '0': return 0
        len_s = len(s)
        memo = [0 for i in range(len_s + 1)]
        memo[len_s] = 1
        if s[-1] == '0':
            memo[len_s - 1] = 0
        else:
            memo[len_s - 1] = 1

        for i in range(2, len_s + 1):
            index = len_s - i
            if s[index] == '0':
                continue
            elif int(s[index] + s[index + 1]) <= 26:
                memo[index] = memo[index + 1] + memo[index + 2]
            else:
                memo[index] = memo[index + 1]
        return memo[0]


mySolution = Solution()
s = '123'
re = mySolution.numDecodings(s)
print(re)
