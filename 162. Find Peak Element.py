'''
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''
'''
O(n)
'''

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        len_nums = len(nums)
        for i in range(len_nums - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len_nums - 1


mySolution = Solution()
nums = []
re = mySolution.findPeakElement(nums)
print(re)
