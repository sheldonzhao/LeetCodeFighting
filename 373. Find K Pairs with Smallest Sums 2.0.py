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
result: beats 3%
method: brute force, maintain a heap which has k elements
time: O(len(num1)*len(num2)*klogk)
space: O(k)
optimization: i < range(min(len(num1),k)) j < range(min(len(num2),k))
TODO：improve efficiency
'''


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        heap = []
        for i in nums1:
            for j in nums2:
                if len(heap) < k:
                    heap.append([i, j])
                    heap.sort(key=sum)
                else:
                    if i + j < heap[-1][0] + heap[-1][1]:
                        heap.pop()
                        heap.append([i, j])
                        heap.sort(key=sum)
        return heap


mySolution = Solution()
num1 = [-10, -4]
num2 = [3, 5, 6, 7, 8, 100]
re = mySolution.kSmallestPairs(num1, num2, 10)
print(re)
