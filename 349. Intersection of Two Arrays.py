'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Each element in the result must be unique.
The result can be in any order.
'''


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2: return []
        h1 = {}
        h2 = {}
        for i in nums1:
            if i not in h1:
                h1[i] = 1
        for i in nums2:
            if i not in h2:
                h2[i] = 1
        res = []
        for i in h1.keys():
            if i in h2:
                res.append(i)
        return res
