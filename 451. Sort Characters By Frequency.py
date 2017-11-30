'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:
"tree"
Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
'''
'''
method: hash map
learning point: get key by value from dict
list(hash_map.keys())[list(hash_map.values()).index(max_frequency)]
'''


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        hash_map = {}
        for i in s:
            if i not in hash_map:
                hash_map[i] = s.count(i)
        res = ''
        while hash_map:
            max_frequency = max(hash_map.values())
            index = list(hash_map.keys())[list(hash_map.values()).index(max_frequency)]
            res += index * max_frequency
            del hash_map[index]
        return res


mySolution = Solution()
s = 'tere'
re = mySolution.frequencySort(s)
print(re)
