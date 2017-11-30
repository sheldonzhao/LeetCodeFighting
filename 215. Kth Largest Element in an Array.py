'''
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
'''
# important for interview
method: quick selection
Time: O(n) worst case: O(n**2) optimization: random.shuffle(nums)
'''

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)
        pivot = nums[0]
        left = [l for l in nums if l < pivot]
        right = [r for r in nums if r > pivot]
        len_nums, len_left, len_right = len(nums), len(left), len(right)
        if k <= len_right:
            return self.findKthLargest(right, k)
        elif k <= len_nums - len_left:
            return pivot
        else:
            return self.findKthLargest(left, k - (len_nums - len_left))


mySolution = Solution()
nums = [3, 2, 5, 5, 6, 4]
k = 3
re = mySolution.findKthLargest(nums, k)
print(re)
