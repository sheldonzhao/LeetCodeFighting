'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
'''
method: 1.sort letter in each word 2.hashmap
learning: ''.join(sorted(strs[i]))
sorted function sort the string and transfer string to list
 ''.join transfer list to string
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        hash_map = {}
        for word in strs:
            # sort letter in each string
            s = ''.join(sorted(word))
            if s in hash_map:
                hash_map[s].append(word)
            else:
                hash_map[s] = [word]
        return hash_map.values()

mySolution = Solution()
strs = ["tea", "and", "ate", "eat", "den"]
re = mySolution.groupAnagrams(strs)
print(re)
