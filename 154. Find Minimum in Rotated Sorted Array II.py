'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array may contain duplicates.
'''
'''
time: O(n)
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] == nums[end]:
                end = end - 1
            else:
                end = mid
        return nums[start]


mySolution = Solution()
nums = [4, 5, 6, 7, 0, 1, 1, 2]
nums1 = [1, 3, 3]
nums2 = [3, 3, 1, 3]
re = mySolution.findMin(nums2)
print(re)
