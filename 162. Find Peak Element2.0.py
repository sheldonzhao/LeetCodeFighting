'''
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
'''
'''
O(logn)
'''


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            mid1 = low + (high - low) // 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:
                low = mid2
            else:
                high = mid1
        return low


mySolution = Solution()
nums = [1]
re = mySolution.findPeakElement(nums)
print(re)
