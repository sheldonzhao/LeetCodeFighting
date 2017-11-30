'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3
Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
'''
'''
result: all cases pass, memory limit exceeded
method: brute force
time: O(mn)
space: O(mn)
exe: hash_map[sum]=[[i,j]] sort hash_map.keys(), then output k [i,j]
'''


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        hash_map = {}
        for i in nums1:
            for j in nums2:
                if i + j not in hash_map:
                    hash_map[i + j] = [[i, j]]
                else:
                    hash_map[i + j].append([i, j])
        res = []
        keys = hash_map.keys()
        keys = sorted(keys)
        for key in keys:
            length = len(hash_map[key])
            if length < k:
                k = k - length
                for i in hash_map[key]:
                    res.append(i)
            else:
                for i in range(k):
                    res.append(hash_map[key][i])
                break
        return res


mySolution = Solution()
num1 = [1, 1, 2]
num2 = [1, 2, 3]
re = mySolution.kSmallestPairs(num1, num2, 2)
print(re)
